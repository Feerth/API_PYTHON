from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services.interfaces.venta_service import IVentaService
from app.repositories.venta_repository import venta_repo
from app.repositories.producto_repository import producto_repo
from app.models.venta import Venta, DetalleVenta
from app.schemas.venta import VentaCreate

class VentaServiceImpl(IVentaService):
    
    def registrar_venta(self, db: Session, venta_in: VentaCreate):
        """
        Registra una nueva venta, valida stock y crea detalles.

        Args:
            db (Session): Sesión de base de datos.
            venta_in (VentaCreate): Datos de la venta.

        Returns:
            Venta: El objeto venta creado.

        Raises:
            HTTPException: Si el producto no es encontrado o hay stock insuficiente.
        """
        monto_total_calculado = 0.0
        lista_detalles_db = []

        # 1. Iteramos los productos del carrito
        for item in venta_in.detalles:
            # Buscar producto para ver precio real y stock
            producto_db = producto_repo.get_by_id(db, item.producto_id)
            
            if not producto_db:
                raise HTTPException(status_code=404, detail=f"Producto {item.producto_id} no encontrado")

            # Validar Stock
            if producto_db.stock < item.cantidad:
                raise HTTPException(status_code=400, detail=f"Stock insuficiente para '{producto_db.nombre}'. Quedan: {producto_db.stock}")

            # Calcular subtotal con precio de la BD
            subtotal = producto_db.precio * item.cantidad
            monto_total_calculado += subtotal

            # Crear detalle (aún en memoria)
            detalle_nuevo = DetalleVenta(
                producto_id=item.producto_id,
                cantidad=item.cantidad,
                precio_unitario=producto_db.precio,
                subtotal=subtotal
            )
            lista_detalles_db.append(detalle_nuevo)

            # Descontar Stock (Memoria)
            producto_db.stock -= item.cantidad

        # 2. Crear Venta Cabecera
        nueva_venta = Venta(
            cliente_id=venta_in.cliente_id,
            empleado_id=venta_in.empleado_id,
            monto_total=monto_total_calculado,
            detalles=lista_detalles_db # SQLAlchemy guarda los detalles automáticamente
        )

        # 3. Guardar todo en la BD
        return venta_repo.create(db, obj_in=nueva_venta)

venta_service = VentaServiceImpl()
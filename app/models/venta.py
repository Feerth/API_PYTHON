from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base


class Venta(Base):
    """
    Representa una transacción de venta.

    Atributos:
        id (int): Clave primaria.
        fecha (datetime): Fecha y hora de la venta.
        monto_total (float): Monto total de la venta.
        cliente_id (int): ID del cliente (opcional).
        empleado_id (int): ID del empleado que realizó la venta.
        cliente (Cliente): Relación con el modelo Cliente.
        empleado (Empleado): Relación con el modelo Empleado.
        detalles (List[DetalleVenta]): Lista de detalles de la venta.
    """
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    monto_total = Column(Float, default=0.0)

    # Claves Foráneas
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=True)
    empleado_id = Column(Integer, ForeignKey("empleados.id"), nullable=False)

    # Relaciones ORM
    cliente = relationship("Cliente")
    empleado = relationship("Empleado")
    detalles = relationship("DetalleVenta", back_populates="venta", cascade="all, delete")


class DetalleVenta(Base):
    """
    Representa un ítem o línea de detalle en una venta.

    Atributos:
        id (int): Clave primaria.
        venta_id (int): Clave foránea a la venta.
        producto_id (int): Clave foránea al producto.
        cantidad (int): Cantidad vendida.
        precio_unitario (float): Precio por unidad al momento de la venta.
        subtotal (float): Subtotal calculado (cantidad * precio_unitario).
        venta (Venta): Relación con la Venta padre.
        producto (Producto): Relación con el Producto.
    """
    __tablename__ = "detalle_ventas"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))

    cantidad = Column(Integer, nullable=False)
    # Precio unitario guardado aquí para preservar historial si el producto cambia de precio
    precio_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)

    venta = relationship("Venta", back_populates="detalles")
    producto = relationship("Producto")
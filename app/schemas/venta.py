from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional
from datetime import datetime
from app.schemas.producto import ProductoResponse
from app.schemas.cliente import ClienteResponse
from app.schemas.empleado import EmpleadoResponse

# --- DETALLE DE VENTA (Items) ---

class DetalleVentaCreate(BaseModel):
    """
    Schema para crear un detalle de venta.

    Atributos:
        producto_id (int): ID del producto.
        cantidad (int): Cantidad a comprar.
    """
    producto_id: int
    cantidad: int = Field(..., gt=0)


class DetalleVentaResponse(BaseModel):
    """
    Schema para responder un detalle de venta.

    Atributos:
        producto_id (int): ID del producto.
        producto (ProductoResponse): Detalles completos del producto.
        cantidad (int): Cantidad vendida.
        precio_unitario (float): Precio unitario al momento de la venta.
        subtotal (float): Subtotal calculado.
    """
    producto_id: int
    producto: ProductoResponse # Anidamos el objeto producto completo
    cantidad: int
    precio_unitario: float
    subtotal: float

    model_config = ConfigDict(from_attributes=True)


# --- VENTA (Header) ---

class VentaCreate(BaseModel):
    """
    Schema para crear una nueva venta.

    Atributos:
        empleado_id (int): ID del empleado que procesa la venta.
        cliente_id (Optional[int]): ID del cliente.
        detalles (List[DetalleVentaCreate]): Lista de ítems a comprar.
    """
    empleado_id: int
    cliente_id: Optional[int] = None
    detalles: List[DetalleVentaCreate]


class VentaResponse(BaseModel):
    """
    Schema para responder una venta.

    Atributos:
        id (int): ID de la venta.
        fecha (datetime): Fecha de la venta.
        monto_total (float): Monto total.
        empleado (EmpleadoResponse): Detalles del empleado.
        cliente (Optional[ClienteResponse]): Detalles del cliente.
        detalles (List[DetalleVentaResponse]): Lista de ítems.
    """
    id: int
    fecha: datetime
    monto_total: float
    empleado: EmpleadoResponse
    cliente: Optional[ClienteResponse] = None
    detalles: List[DetalleVentaResponse] # Lista anidada

    model_config = ConfigDict(from_attributes=True)
from fastapi import APIRouter
from app.api.v1.endpoints import productos, ventas, clientes, empleados, reports

"""
Router de configuración de la API para la Versión 1.
"""

api_router = APIRouter()

api_router.include_router(productos.router, prefix="/productos", tags=["Productos"])
api_router.include_router(clientes.router, prefix="/clientes", tags=["Clientes"])
api_router.include_router(empleados.router, prefix="/empleados", tags=["Empleados"])
api_router.include_router(ventas.router, prefix="/ventas", tags=["Ventas"])
api_router.include_router(reports.router, prefix="/reports", tags=["Reportes"])
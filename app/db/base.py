"""
Importa todos los modelos, para que Base los tenga antes de ser
importados por Alembic.
"""
from app.db.session import Base
from app.models.cliente import Cliente
from app.models.empleado import Empleado
from app.models.producto import Producto
from app.models.venta import Venta

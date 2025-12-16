from sqlalchemy import Column, Integer, String, Float
from app.db.session import Base

class Producto(Base):
    """
    Representa un producto en el inventario.

    Atributos:
        id (int): Clave primaria.
        nombre (str): Nombre del producto.
        descripcion (str): Descripción opcional.
        precio (float): Precio unitario.
        stock (int): Cantidad actual en stock.
    """
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0, nullable=False)
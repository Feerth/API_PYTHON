from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Cliente(Base):
    """
    Representa un cliente en el sistema.

    Atributos:
        id (int): Clave primaria.
        nombre_completo (str): Nombre completo del cliente.
        dni (str): Documento Nacional de Identidad (único).
    """
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, nullable=False)
    dni = Column(String, unique=True, index=True, nullable=False)
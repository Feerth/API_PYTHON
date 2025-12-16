from sqlalchemy import Column, Integer, String, Boolean
from app.db.session import Base

class Empleado(Base):
    """
    Representa un empleado en el sistema.

    Atributos:
        id (int): Clave primaria.
        nombre_completo (str): Nombre completo del empleado.
        dni (str): Documento Nacional de Identidad (único).
        cargo (str): Puesto o cargo del empleado.
    """
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre_completo = Column(String, nullable=False)
    dni = Column(String, unique=True, index=True, nullable=False)
    cargo = Column(String, nullable=True)
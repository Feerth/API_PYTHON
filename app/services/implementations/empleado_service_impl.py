from typing import Optional
from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.repositories.empleado_repository import EmpleadoRepository
from app.schemas.empleado import EmpleadoCreate
from app.services.interfaces.empleado_service import EmpleadoService

class EmpleadoServiceImpl(EmpleadoService):
    def __init__(self):
        self.repository = EmpleadoRepository()

    # Authenticate methods removed

    def create_user(self, db: Session, obj_in: EmpleadoCreate) -> Empleado:
        # Create DB model from schema
        db_obj = Empleado(
            nombre_completo=obj_in.nombre_completo,
            dni=obj_in.dni,
            cargo=obj_in.cargo
        )
        return self.repository.create(db, obj_in=db_obj)
    
    # get_by_email removed or optional if email is kept as info? 
    # Plan said remove email column potentially. 
    # Model update commented it out. So let's remove it here.

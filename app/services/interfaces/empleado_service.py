from abc import ABC, abstractmethod
from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.schemas.empleado import EmpleadoCreate  # Assuming this exists or I need to create it properly

class EmpleadoService(ABC):
    @abstractmethod
    def authenticate(self, db: Session, email: str, password: str) -> Optional[Empleado]:
        pass

    @abstractmethod
    def create_user(self, db: Session, obj_in: EmpleadoCreate) -> Empleado:
        pass
    
    @abstractmethod
    def get_by_email(self, db: Session, email: str) -> Optional[Empleado]:
        pass

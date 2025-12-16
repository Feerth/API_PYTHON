from typing import Optional
from sqlalchemy.orm import Session
from app.models.empleado import Empleado
from app.repositories.base import BaseRepository

class EmpleadoRepository(BaseRepository[Empleado]):
    def __init__(self):
        super().__init__(Empleado)

    def get_by_email(self, db: Session, email: str) -> Optional[Empleado]:
        return db.query(self.model).filter(self.model.email == email).first()
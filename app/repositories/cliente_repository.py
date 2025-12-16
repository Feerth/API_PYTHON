from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.repositories.base import BaseRepository

class ClienteRepository(BaseRepository[Cliente]):
    def __init__(self):
        super().__init__(Cliente)
    
    def get_by_dni(self, db: Session, dni: str):
        return db.query(self.model).filter(self.model.dni == dni).first()

cliente_repo = ClienteRepository()
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.schemas.venta import VentaCreate

class IVentaService(ABC):
    @abstractmethod
    def registrar_venta(self, db: Session, venta_in: VentaCreate):
        pass
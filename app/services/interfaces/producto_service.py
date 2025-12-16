from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from app.schemas.producto import ProductoCreate, ProductoUpdate

class IProductoService(ABC):
    
    @abstractmethod
    def crear_producto(self, db: Session, producto: ProductoCreate):
        pass

    @abstractmethod
    def listar_productos(self, db: Session):
        pass
        
    @abstractmethod
    def obtener_por_id(self, db: Session, producto_id: int):
        pass
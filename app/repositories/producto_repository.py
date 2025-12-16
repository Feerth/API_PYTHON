from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.repositories.base import BaseRepository

class ProductoRepository(BaseRepository[Producto]):
    def __init__(self):
        super().__init__(Producto)

    def buscar_por_nombre(self, db: Session, nombre: str):
        """
        Busca productos por nombre (coincidencia parcial insensible a mayúsculas).
        """
        return db.query(self.model).filter(self.model.nombre.ilike(f"%{nombre}%")).all()

    def get_filtered(self, db: Session, skip: int = 0, limit: int = 100, min_price: float = None, max_price: float = None):
        """
        Recupera productos con filtrado opcional por precio.
        """
        query = db.query(self.model)
        if min_price is not None:
            query = query.filter(self.model.precio >= min_price)
        if max_price is not None:
            query = query.filter(self.model.precio <= max_price)
        return query.offset(skip).limit(limit).all()

producto_repo = ProductoRepository()
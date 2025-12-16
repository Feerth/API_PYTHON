from sqlalchemy.orm import Session
from app.services.interfaces.producto_service import IProductoService
from app.repositories.producto_repository import producto_repo
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate

class ProductoServiceImpl(IProductoService):

    def crear_producto(self, db: Session, producto_in: ProductoCreate):
        # Convertimos el DTO (Pydantic) a Modelo (SQLAlchemy)
        nuevo_producto = Producto(**producto_in.model_dump())
        return producto_repo.create(db, obj_in=nuevo_producto)

    def listar_productos(self, db: Session):
        return producto_repo.get_all(db)

    def obtener_por_id(self, db: Session, producto_id: int):
        return producto_repo.get_by_id(db, producto_id)

producto_service = ProductoServiceImpl()
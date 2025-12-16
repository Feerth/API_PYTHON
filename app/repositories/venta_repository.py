from sqlalchemy.orm import Session
from app.models.venta import Venta
from app.repositories.base import BaseRepository

class VentaRepository(BaseRepository[Venta]):
    def __init__(self):
        super().__init__(Venta)

    def get_all_con_detalles(self, db: Session):
        """
        Recupera todas las ventas con carga ansiosa (eager loading) de detalles.

        Args:
            db (Session): Sesión de base de datos.
        """
        return db.query(self.model).all() 

venta_repo = VentaRepository()
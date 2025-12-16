from typing import Generic, TypeVar, Type, List, Optional, Any
from sqlalchemy.orm import Session
from app.db.session import Base

# Generic Type T (Base model subclass)
T = TypeVar('T', bound=Base)

class BaseRepository(Generic[T]):
    """
    Clase Base Repository que implementa operaciones CRUD comunes.
    """
    def __init__(self, model: Type[T]):
        """
        Inicializa el repositorio con la clase del modelo.

        Args:
            model (Type[T]): La clase del modelo SQLAlchemy.
        """
        self.model = model

    def get_by_id(self, db: Session, id: Any) -> Optional[T]:
        """
        Recupera un registro por su ID.

        Args:
            db (Session): Sesión de base de datos.
            id (Any): ID del registro.

        Returns:
            Optional[T]: El registro si se encuentra, o None.
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[T]:
        """
        Recupera todos los registros con paginación.

        Args:
            db (Session): Sesión de base de datos.
            skip (int): Número de registros a saltar.
            limit (int): Número máximo de registros a retornar.

        Returns:
            List[T]: Lista de registros.
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: T) -> T:
        """
        Crea un nuevo registro.

        Args:
            db (Session): Sesión de base de datos.
            obj_in (T): El objeto a crear.

        Returns:
            T: El objeto creado.
        """
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in
        
    def delete(self, db: Session, id: Any) -> bool:
        """
        Elimina un registro por ID.

        Args:
            db (Session): Sesión de base de datos.
            id (Any): ID del registro.

        Returns:
            bool: True si se eliminó, False si no se encontró.
        """
        obj = self.get_by_id(db, id)
        if obj:
            db.delete(obj)
            db.commit()
            return True
        return False
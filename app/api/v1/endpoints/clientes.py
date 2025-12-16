from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.cliente import ClienteCreate, ClienteResponse
from app.repositories.cliente_repository import cliente_repo

router = APIRouter()

@router.post("/", response_model=ClienteResponse)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo cliente.

    Args:
        cliente (ClienteCreate): Datos del cliente.
        db (Session): Sesión de base de datos.

    Returns:
        ClienteResponse: El cliente creado.
    """
    return cliente_repo.create(db, cliente)

@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    return cliente_repo.get_all(db, skip=skip, limit=limit)
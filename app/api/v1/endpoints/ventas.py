from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.venta import VentaCreate, VentaResponse
from app.services.implementations.venta_service_impl import venta_service

router = APIRouter()

@router.post("/", response_model=VentaResponse)
def registrar_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    """
    Registra una nueva venta, actualiza stock y calcula total.

    Args:
        venta (VentaCreate): Datos de la venta.
        db (Session): Sesión de base de datos.

    Returns:
        VentaResponse: La venta registrada.
    """
    return venta_service.registrar_venta(db, venta)

@router.get("/", response_model=List[VentaResponse])
def listar_ventas(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Lista todas las ventas con paginación.
    """
    from app.repositories.venta_repository import venta_repo
    return venta_repo.get_all(db, skip=skip, limit=limit)
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.producto import ProductoCreate, ProductoResponse
from app.repositories.producto_repository import producto_repo

router = APIRouter()

@router.get("/", response_model=List[ProductoResponse])
def listar_productos(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    min_price: float = None,
    max_price: float = None
):
    return producto_repo.get_filtered(db, skip=skip, limit=limit, min_price=min_price, max_price=max_price)

@router.post("/", response_model=ProductoResponse)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    return producto_repo.create(db, producto)
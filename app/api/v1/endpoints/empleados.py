from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.empleado import EmpleadoCreate, EmpleadoResponse
from app.services.implementations.empleado_service_impl import EmpleadoServiceImpl
from app.models.empleado import Empleado

router = APIRouter()

@router.post("/", response_model=EmpleadoResponse)
def crear_empleado(
    empleado: EmpleadoCreate, 
    db: Session = Depends(get_db)
):
    service = EmpleadoServiceImpl()
    return service.create_user(db, empleado)

@router.get("/", response_model=List[EmpleadoResponse])
def listar_empleados(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    service = EmpleadoServiceImpl()
    return service.repository.get_all(db, skip=skip, limit=limit)
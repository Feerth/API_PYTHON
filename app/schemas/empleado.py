from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
from typing import Optional

class EmpleadoBase(BaseModel):
    nombre_completo: str
    dni: str
    cargo: Optional[str] = "Cajero"

    @field_validator('dni')
    @classmethod
    def validate_dni(cls, v: str) -> str:
        if not (8 <= len(v) <= 10):
            raise ValueError('El DNI debe tener entre 8 y 10 caracteres')
        return v

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoResponse(EmpleadoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

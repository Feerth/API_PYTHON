from pydantic import BaseModel, ConfigDict, field_validator
import re

class ClienteBase(BaseModel):
    """
    Schema base para Cliente.

    Atributos:
        nombre_completo (str): Nombre completo del cliente.
        dni (str): Documento Nacional de Identidad.
    """
    nombre_completo: str
    dni: str

    @field_validator('dni')
    @classmethod
    def validate_dni(cls, v: str) -> str:
        """
        Valida el formato del DNI.
        """
        if not re.match(r'^\d{8}[A-Z]$', v) and not re.match(r'^\d{9}$', v) and not re.match(r'^\d{8}$', v):
             # Simplified validation: 8-10 chars
             if not (8 <= len(v) <= 10):
                raise ValueError('El DNI debe tener entre 8 y 10 caracteres')
        return v

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
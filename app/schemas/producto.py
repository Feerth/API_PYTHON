from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

# Base: Atributos compartidos (para crear y leer)
class ProductoBase(BaseModel):
    nombre: str = Field(..., min_length=1, example="Arroz Costeño 1kg")
    descripcion: Optional[str] = None
    precio: float = Field(..., gt=0, example=4.50)
    stock: int = Field(default=0, ge=0)

# Create: Lo que necesitamos para crear un producto (igual a la base)
class ProductoCreate(ProductoBase):
    pass

# Update: Para actualizar (todo opcional)
class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    precio: Optional[float] = None
    stock: Optional[int] = None

# Response: Lo que devolvemos al cliente (incluye ID)
class ProductoResponse(ProductoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

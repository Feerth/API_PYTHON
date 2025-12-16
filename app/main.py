from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.api import api_router
from app.core.logging import setup_logging
import logging

# Configurar logs
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:3000", # React/Vue dev
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Exception Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"},
    )

# Incluimos todas las rutas (Ventas, Productos, etc)
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    logger.info("Health check endpoint called")
    return {"mensaje": "API Supermercado Activa", "docs": "/docs"}
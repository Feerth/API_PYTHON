from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Configuración para SQLite (necesario para hilos)
connect_args = {"check_same_thread": False}

engine = create_engine(
    settings.DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia para obtener la DB en cada petición
# Dependencia para obtener la sesión de DB en cada petición
def get_db():
    """
    Generador de dependencias para sesiones de base de datos.

    Yields:
        Session: Una sesión de base de datos SQLAlchemy.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
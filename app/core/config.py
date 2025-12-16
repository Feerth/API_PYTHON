from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Configuraciones de la aplicación.

    Atributos:
        PROJECT_NAME (str): Nombre del proyecto.
        DATABASE_URL (str): URL de conexión a la base de datos.
        API_V1_STR (str): Cadena de versión de la API.
        SECRET_KEY (str): Clave secreta para seguridad.
        ALGORITHM (str): Algoritmo usado para encriptación.
        ACCESS_TOKEN_EXPIRE_MINUTES (int): Tiempo de expiración del token en minutos.
    """
    PROJECT_NAME: str
    DATABASE_URL: str
    API_V1_STR: str
    SECRET_KEY: str = "supersecretkeyshouldbechanged"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore"
    )

settings = Settings()
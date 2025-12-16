import logging
import sys

def setup_logging():
    """
    Configura el logging de la aplicación.

    Establece el nivel de log a INFO y formatea la salida.
    Reduce la verbosidad para librerías de terceros como uvicorn y sqlalchemy.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.WARNING)

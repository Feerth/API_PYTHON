# 🛒 Supermercado API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-black?style=for-the-badge&logo=sqlalchemy&logoColor=red)
![Pydantic](https://img.shields.io/badge/Pydantic-e92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-black?style=for-the-badge&logo=alembic)

**API Profesional de Gestión de Supermercado**

Una API REST robusta, moderna y escalable construida con **Python 3.10+** y **FastAPI**. Diseñada para gestionar integralmente las operaciones de un supermercado, desde el control de inventario hasta la emisión de ventas y reportes analíticos.

Este proyecto sigue los más altos estándares de desarrollo backend, implementando arquitecturas limpias y patrones de diseño empresariales.

---

## 🚀 Características Clave

- **Gestión de Inventario en Tiempo Real**: Control preciso de stock con validaciones atómicas para prevenir sobreventas.
- **Procesamiento de Ventas Transaccional**: Registro de ventas complejas (múltiples ítems) asegurando la integridad de datos mediante transacciones de base de datos.
- **Validación de Datos Estricta**: Uso intensivo de **Pydantic** para validar entradas, formatos de DNI, precios positivos y más, garantizando que solo datos limpios entren al sistema.
- **Paginación y Filtrado Avanzado**: Endpoints optimizados para alto rendimiento, permitiendo filtrar productos por rango de precios y navegar grandes listas de datos.
- **Inteligencia de Negocio (BI)**: Módulos de reportes dedicados para identificar productos estrella y analizar tendencias de ingresos.
- **Arquitectura Limpia (Clean Architecture)**: Separación clara de responsabilidades en capas:
  - **API Layer**: Controladores y endpoints.
  - **Service Layer**: Lógica de negocio pura.
  - **Repository Layer**: Abstracción del acceso a datos.
  - **Domain Layer**: Modelos y esquemas.
- **Base de Datos Evolutiva**: Gestión de cambios en el esquema de base de datos mediante migraciones automatizadas con **Alembic**.
- **Integración Frontend-Ready**: Configuración CORS lista para conectar con aplicaciones React, Vue, Angular o móviles.

## 🛠️ Stack Tecnológico

- **Framework Web**: [FastAPI](https://fastapi.tiangolo.com/) - Rendimiento asíncrono superior.
- **Lenguaje**: Python 3.10+.
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) - Potente mapeo objeto-relacional.
- **Migraciones**: [Alembic](https://alembic.sqlalchemy.org/).
- **Esquemas y Validación**: [Pydantic v2](https://docs.pydantic.dev/).
- **Testing**: [Pytest](https://docs.pytest.org/).

## 📦 Instalación y Configuración

Sigue estos pasos para desplegar el proyecto en tu entorno local:

### 1. Prerrequisitos

Asegúrate de tener instalado Python 3.10 o superior.

### 2. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/supermercado-api.git
cd supermercado-api
```

### 3. Configurar el entorno virtual

Es buena práctica aislar las dependencias del proyecto.

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
.\venv\Scripts\activate

# Activar entorno (macOS/Linux)
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```
## ▶️ Ejecución

Para iniciar el servidor de desarrollo con recarga automática (hot-reload):

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en: `http://127.0.0.1:8000`

## 📖 Documentación Interactiva

FastAPI genera documentación automática basada en el estándar OpenAPI. Una vez iniciado el servidor, puedes acceder a:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Explora y prueba los endpoints interactivamente.
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) - Documentación alternativa visualmente atractiva.

### Endpoints Principales

| Método | Endpoint                       | Descripción                                          |
| :----- | :----------------------------- | :--------------------------------------------------- |
| `GET`  | `/api/v1/productos/`           | Listar productos con filtros de precio y paginación. |
| `POST` | `/api/v1/ventas/`              | Registrar una nueva venta (carrito de compras).      |
| `GET`  | `/api/v1/clientes/`            | Gestión de clientes.                                 |
| `GET`  | `/api/v1/reports/top-products` | Reporte de productos más vendidos.                   |

## 🧪 Testing

Para verificar la integridad del sistema y la lógica de negocio, ejecuta la suite de pruebas automatizadas:

```bash
# Ejecutar todos los tests
python -m pytest tests

# Ejecutar con salida detallada
python -m pytest tests -v
```

## 📂 Estructura del Proyecto

```
API_PYTHON/
├── alembic/              # Scripts de migración de base de datos
├── app/
│   ├── api/              # Capa de presentación (Endpoints)
│   ├── core/             # Configuración global (Logging, Settings)
│   ├── db/               # Configuración de BD y Session Factory
│   ├── models/           # Modelos de dominio (SQLAlchemy)
│   ├── repositories/     # Capa de acceso a datos (Patrón Repositorio)
│   ├── schemas/          # DTOs y validación (Pydantic)
│   ├── services/         # Lógica de negocio compleja (Service Layer)
│   └── main.py           # Punto de entrada de la aplicación
├── tests/                # Tests unitarios y de integración
├── alembic.ini           # Configuración de Alembic
├── requirements.txt      # Lista de dependencias
└── README.md             # Documentación del proyecto
```


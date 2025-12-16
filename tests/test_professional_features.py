from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.producto import Producto

def test_pagination_products(client: TestClient, db_session: Session):
    # Create 15 products
    for i in range(15):
        db_session.add(Producto(nombre=f"Prod {i}", precio=10.0, stock=100))
    db_session.commit()

    # Get first 10 (default)
    response = client.get("/api/v1/productos/?limit=10")
    assert len(response.json()) == 10
    
    # Get next 5
    response = client.get("/api/v1/productos/?skip=10&limit=10")
    assert len(response.json()) == 5

def test_analytics_endpoints(client: TestClient, db_session: Session):
    response = client.get("/api/v1/reports/daily-stats")
    assert response.status_code == 200
    assert "total_ventas_count" in response.json()
    assert "total_ingresos" in response.json()

def test_validation_failure(client: TestClient):
    # Test invalid DNI (too short)
    response = client.post(
        "/api/v1/clientes/",
        json={"nombre_completo": "Test Bad DNI", "dni": "123"} 
    )
    assert response.status_code == 422
    
    # Test invalid Price (negative)
    response = client.post(
        "/api/v1/productos/",
        json={"nombre": "Bad Price", "precio": -5.0, "stock": 10}
    )
    assert response.status_code == 422

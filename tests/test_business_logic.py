from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.models.empleado import Empleado
from app.api.deps import get_db

def test_stock_reduction(client: TestClient, db_session: Session):
    # 1. Create Product with initial stock
    producto = Producto(nombre="Cookie", precio=1.50, stock=10)
    db_session.add(producto)
    
    # Create Empleado (needed for Venta)
    empleado = Empleado(nombre_completo="Seller", dni="99988877X")
    db_session.add(empleado)
    db_session.commit()
    db_session.refresh(producto)
    db_session.refresh(empleado)
    
    initial_stock = producto.stock

    # 2. Perform Sale
    response = client.post(
        "/api/v1/ventas/",
        json={
            "cliente_id": None, # Optional
            "empleado_id": empleado.id,
            "detalles": [
                {"producto_id": producto.id, "cantidad": 2}
            ]
        }
    )
    
    assert response.status_code == 200, response.text

    # 3. Verify Stock Reduced
    db_session.refresh(producto)
    assert producto.stock == initial_stock - 2

def test_insufficient_stock(client: TestClient, db_session: Session):
    # 1. Create Product
    producto = Producto(nombre="Rare Item", precio=100.0, stock=1)
    db_session.add(producto)
    empleado = Empleado(nombre_completo="Seller 2", dni="11122233Z")
    db_session.add(empleado)
    db_session.commit()
    db_session.refresh(producto)
    db_session.refresh(empleado)

    # 2. Try to sell more than stock
    response = client.post(
        "/api/v1/ventas/",
        json={
            "empleado_id": empleado.id,
            "detalles": [
                {"producto_id": producto.id, "cantidad": 5}
            ]
        }
    )
    
    assert response.status_code == 400
    assert "Stock insuficiente" in response.json()["detail"]

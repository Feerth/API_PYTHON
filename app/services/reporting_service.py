from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Dict, Any
from app.models.venta import Venta, DetalleVenta
from app.models.producto import Producto

class ReportingService:
    def get_top_selling_products(self, db: Session, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Retorna los productos más vendidos por cantidad.

        Args:
            db (Session): Sesión de base de datos.
            limit (int): Número máximo de productos a retornar.
        """
        results = db.query(
            Producto.nombre,
            func.sum(DetalleVenta.cantidad).label("total_vendido")
        ).join(DetalleVenta, Producto.id == DetalleVenta.producto_id)\
         .group_by(Producto.id)\
         .order_by(func.sum(DetalleVenta.cantidad).desc())\
         .limit(limit).all()
        
        return [{"producto": r[0], "total_vendido": r[1]} for r in results]

    def get_daily_sales_stats(self, db: Session) -> Dict[str, Any]:
        """
        Returns total count of sales and total revenue for today (or general stats for simplicity).
        For simplicity, let's return all-time stats first.
        """
        total_ventas = db.query(func.count(Venta.id)).scalar()
        total_ingresos = db.query(func.sum(Venta.monto_total)).scalar() or 0.0
        
        return {
            "total_ventas_count": total_ventas,
            "total_ingresos": total_ingresos
        }

reporting_service = ReportingService()

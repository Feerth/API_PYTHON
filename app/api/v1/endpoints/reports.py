from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.db.session import get_db
from app.services.reporting_service import reporting_service

router = APIRouter()

@router.get("/top-products", response_model=List[Dict[str, Any]])
def get_top_selling_products(limit: int = 5, db: Session = Depends(get_db)):
    """
    Get top selling products by total quantity sold.
    """
    return reporting_service.get_top_selling_products(db, limit=limit)

@router.get("/daily-stats")
def get_daily_stats(db: Session = Depends(get_db)):
    """
    Get general sales statistics.
    """
    return reporting_service.get_daily_sales_stats(db)

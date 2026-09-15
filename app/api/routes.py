from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import SessionLocal
from app.schemas.stock import StockCreate
from app.repositories import stock_repo


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/stocks")
def get_stocks(db: Session = Depends(get_db)):
    return stock_repo.get_all_stocks(db)


@router.get("/stocks/{ticker}")
def get_stock(ticker: str, db: Session = Depends(get_db)):
    stock = stock_repo.get_stock(db, ticker)

    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    return stock


@router.post("/stocks")
def create_stock(stock: StockCreate, db: Session = Depends(get_db)):
    return stock_repo.create_stock(db, stock)


@router.put("/stocks/{ticker}")
def update_stock(ticker: str, stock: StockCreate, db: Session = Depends(get_db)):
    updated_stock = stock_repo.update_stock(db, ticker, stock)

    if not updated_stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    return updated_stock


@router.delete("/stocks/{ticker}")
def delete_stock(ticker: str, db: Session = Depends(get_db)):
    stock = stock_repo.delete_stock(db, ticker)

    if not stock:
        raise HTTPException(status_code=404, detail="Stock not found")

    return {"message": "Stock deleted"}

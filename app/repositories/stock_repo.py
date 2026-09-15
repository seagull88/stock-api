from sqlalchemy.orm import Session

from app.models.stock import Stock
from app.schemas.stock import StockCreate


def get_all_stocks(db: Session):
    return db.query(Stock).all()


def get_stock(db: Session, ticker: str):
    return db.query(Stock).filter(
        Stock.ticker == ticker.upper()
    ).first()


def create_stock(db: Session, stock: StockCreate):
    new_stock = Stock(
        ticker=stock.ticker.upper(),
        company=stock.company,
        price=stock.price,
    )

    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)

    return new_stock


def update_stock(db: Session, ticker: str, stock_data: StockCreate):
    stock = get_stock(db, ticker)

    if not stock:
        return None

    stock.ticker = stock_data.ticker.upper()
    stock.company = stock_data.company
    stock.price = stock_data.price

    db.commit()
    db.refresh(stock)

    return stock


def delete_stock(db: Session, ticker: str):
    stock = get_stock(db, ticker)

    if not stock:
        return None

    db.delete(stock)
    db.commit()

    return stock

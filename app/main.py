from fastapi import FastAPI

from app.database.db import Base, engine
from app.api.routes import router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Stock API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Stock API is running"}
""" changes in files"""

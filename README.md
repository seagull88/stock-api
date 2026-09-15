# Stock API

REST API for managing stock data built with FastAPI, PostgreSQL, SQLAlchemy and Docker.

## Technologies

- Python
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- Pydantic
- Docker
- Docker Compose

## API Endpoints

- GET /stocks
- GET /stocks/{ticker}
- POST /stocks
- PUT /stocks/{ticker}
- DELETE /stocks/{ticker}

## Run

docker compose up --build

API:
http://localhost:8001

Swagger:
http://localhost:8001/docs

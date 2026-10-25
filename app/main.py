from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.api import books, categories
from app.db.db import engine


@asynccontextmanager
async def lifespan(app):
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    yield
    engine.dispose()


app = FastAPI(title="API книг и категорий", lifespan=lifespan)
app.include_router(categories.router)
app.include_router(books.router)


@app.get("/health", tags=["health"])
def health():
    return {"status": "ok"}

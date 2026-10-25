from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session

from app.db import crud
from app.db.db import get_db
from app.schemas import BookCreate, BookRead, BookUpdate


router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=list[BookRead])
def read_books(category_id: int | None = Query(default=None, gt=0), db: Session = Depends(get_db)):
    return crud.get_books(db, category_id)


@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book


@router.post("", response_model=BookRead, status_code=201)
def add_book(data: BookCreate, db: Session = Depends(get_db)):
    if crud.get_category(db, data.category_id) is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return crud.create_book(db, **data.model_dump())


@router.put("/{book_id}", response_model=BookRead)
def edit_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    if crud.get_book(db, book_id) is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    if crud.get_category(db, data.category_id) is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return crud.update_book(db, book_id, **data.model_dump())


@router.delete("/{book_id}", status_code=204)
def remove_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return Response(status_code=204)

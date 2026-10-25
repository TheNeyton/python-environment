from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db import crud
from app.db.db import get_db
from app.schemas import CategoryCreate, CategoryRead, CategoryUpdate


router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("", response_model=list[CategoryRead])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


@router.get("/{category_id}", response_model=CategoryRead)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category


@router.post("", response_model=CategoryRead, status_code=201)
def add_category(data: CategoryCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_category(db, data.title)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Такая категория уже есть")


@router.put("/{category_id}", response_model=CategoryRead)
def edit_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    try:
        category = crud.update_category(db, category_id, data.title)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Такая категория уже есть")
    if category is None:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return category


@router.delete("/{category_id}", status_code=204)
def remove_category(category_id: int, db: Session = Depends(get_db)):
    if not crud.delete_category(db, category_id):
        raise HTTPException(status_code=404, detail="Категория не найдена")
    return Response(status_code=204)

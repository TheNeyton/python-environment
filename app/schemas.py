from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class CategoryBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class BookBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: str
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    url: str = Field(default="", max_length=500)
    category_id: int = Field(gt=0)


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class BookRead(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

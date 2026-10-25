from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship

from .db import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    books = relationship("Book", back_populates="category", cascade="all, delete-orphan")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    url = Column(String(500), default="", nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="books")

from db.crud import get_books, get_categories
from db.db import SessionLocal


def main():
    db = SessionLocal()
    try:
        categories = get_categories(db)
        books = get_books(db)

        print("Книги из PostgreSQL")
        for category in categories:
            print(f"\nКатегория: {category.title}")
            for book in books:
                if book.category_id == category.id:
                    print(f"{book.id}. {book.title} — {book.price:.2f} руб.")
                    print(f"   {book.description}")
    finally:
        db.close()


if __name__ == "__main__":
    main()

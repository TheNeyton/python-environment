from db.db import Base, SessionLocal, engine
from db.models import Book, Category


def main():
    Base.metadata.create_all(engine)
    db = SessionLocal()
    try:
        if db.query(Category).count() > 0:
            print("Данные уже добавлены")
            return

        programming = Category(title="Программирование")
        fiction = Category(title="Художественная литература")

        programming.books = [
            Book(title="Python для начинающих", description="Основы языка Python", price=650),
            Book(title="Алгоритмы на Python", description="Примеры задач и алгоритмов", price=850),
            Book(title="Базы данных", description="Введение в SQL и PostgreSQL", price=700),
        ]
        fiction.books = [
            Book(title="Мастер и Маргарита", description="Роман Михаила Булгакова", price=550),
            Book(title="Капитанская дочка", description="Повесть Александра Пушкина", price=450),
            Book(title="Герой нашего времени", description="Роман Михаила Лермонтова", price=500),
        ]

        db.add_all([programming, fiction])
        db.commit()
        print("Добавлены 2 категории и 6 книг")
    finally:
        db.close()


if __name__ == "__main__":
    main()

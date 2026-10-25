from .models import Book, Category


def create_category(db, title):
    category = Category(title=title)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category


def get_categories(db):
    return db.query(Category).order_by(Category.id).all()


def get_category(db, category_id):
    return db.get(Category, category_id)


def update_category(db, category_id, title):
    category = get_category(db, category_id)
    if category is None:
        return None
    category.title = title
    db.commit()
    db.refresh(category)
    return category


def delete_category(db, category_id):
    category = get_category(db, category_id)
    if category is None:
        return False
    db.delete(category)
    db.commit()
    return True


def create_book(db, title, description, price, category_id, url=""):
    book = Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_books(db):
    return db.query(Book).order_by(Book.id).all()


def get_book(db, book_id):
    return db.get(Book, book_id)


def update_book(db, book_id, title, description, price, category_id, url=""):
    book = get_book(db, book_id)
    if book is None:
        return None
    book.title = title
    book.description = description
    book.price = price
    book.category_id = category_id
    book.url = url
    db.commit()
    db.refresh(book)
    return book


def delete_book(db, book_id):
    book = get_book(db, book_id)
    if book is None:
        return False
    db.delete(book)
    db.commit()
    return True

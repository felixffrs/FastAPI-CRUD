from sqlalchemy.orm import Session
from schemas import book_schemas, review_schemas
from models.review import Review
from models.book import Book
from fastapi import HTTPException

def create_book(db: Session, book: book_schemas.BookCreate) -> Book:
    db_book = Book(title=book.title, pages=book.pages, isbn_code=book.isbn_code, author_id=book.author_id) 
    db.add(db_book)
    db.commit()
    return db_book

def get_all_books(db: Session) -> list[Book]:
    books = db.query(Book).all()
    return books

def get_book_by_id(db: Session, id: int) -> Book:
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException(404, {
            "message": f"Book id {id} not found"
        })
    return book

def create_book_review(db: Session, book_id: int, review: review_schemas.ReviewCreate) -> Review:
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(404, {
            "message": f"Book id {book_id} not found"
        })
    db_review = Review(rating=review.rating, description=review.description, book_id=book_id)
    db.add(db_review)
    db.commit()
    return db_review

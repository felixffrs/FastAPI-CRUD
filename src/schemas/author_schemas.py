from pydantic import BaseModel
from datetime import date
from schemas.book_schemas import Book

class AuthorBase(BaseModel):
    name: str
    birth_date: date
    biography: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: list[Book] = []
    
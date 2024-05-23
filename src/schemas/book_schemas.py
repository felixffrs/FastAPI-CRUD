from pydantic import BaseModel
from schemas.review_schemas import Review

class BookBase(BaseModel):
    title: str
    pages: int
    isbn_code: str

class BookCreate(BookBase):
    author_id: int

class Book(BookBase):
    id: int
    author_id: int
    reviews: list[Review] = []
    
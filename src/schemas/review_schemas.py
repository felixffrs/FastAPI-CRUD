from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: str
    description: int

class ReviewCreate(ReviewBase):
    book_id: int

class Review(ReviewBase):
    id: int
    book_id: int
    
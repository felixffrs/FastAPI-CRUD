from pydantic import BaseModel

class ReviewBase(BaseModel):
    rating: int
    description: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int
    
from fastapi import APIRouter, Depends
from schemas import book_schemas, review_schemas
from sqlalchemy.orm import Session
from database import get_db
from cruds import book_crud
from dependencies import get_token

router = APIRouter(
    prefix="/api/v1/books",
    tags=["books"],
    dependencies=[Depends(get_token)],
    responses={404: {"description": "Not found"}},
)

@router.post("", response_model=book_schemas.Book)
def create_book(book: book_schemas.BookCreate, db: Session = Depends(get_db)): 
    return book_crud.create_book(db=db, book=book)

@router.get("", response_model=list[book_schemas.Book])
def get_all_books(db: Session = Depends(get_db)): 
    return book_crud.get_all_books(db=db)

@router.get("/{id}", response_model=book_schemas.Book)
def get_book_by_id(id: int, db: Session = Depends(get_db)): 
    return book_crud.get_book_by_id(db=db, id=id)

@router.post("/{id}/reviews", response_model=review_schemas.Review)
def create_book_review(id: int, review: review_schemas.ReviewCreate, db: Session = Depends(get_db)): 
    return book_crud.create_book_review(db=db, book_id=id, review=review)

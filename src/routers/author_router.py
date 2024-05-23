from fastapi import APIRouter, Depends, HTTPException
from schemas import author_schemas
from sqlalchemy.orm import Session
from database import get_db
from cruds import author_crud
from dependencies import get_token

router = APIRouter(
    prefix="/api/v1/authors",
    tags=["authors"],
    dependencies=[Depends(get_token)],
    responses={404: {"description": "Not found"}},
)

@router.post("", response_model=author_schemas.Author)
def create_author(author: author_schemas.AuthorCreate, db: Session = Depends(get_db)): 
    return author_crud.create_author(db=db, author=author)
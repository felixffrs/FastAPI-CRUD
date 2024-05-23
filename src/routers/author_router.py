from fastapi import APIRouter, Depends, HTTPException
from schemas import author_schemas
from sqlalchemy.orm import Session
from database import get_db
from cruds.author_crud import create_user
from dependencies import get_token

router = APIRouter(
    prefix="/api/v1/authors",
    tags=["authors"],
    dependencies=[Depends(get_token)],
    responses={404: {"description": "Not found"}},
)

@router.post("", response_model=author_schemas.Author)
def create_user_endopint(author: author_schemas.AuthorCreate, db: Session = Depends(get_db)): 
    return create_user(db=db, author=author)
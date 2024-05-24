from fastapi import APIRouter, Depends
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

@router.get("", response_model=list[author_schemas.Author])
def get_all_authors(db: Session = Depends(get_db)): 
    return author_crud.get_all_authors(db=db)

@router.get("/{id}", response_model=author_schemas.Author)
def get_author_by_id(id: int, db: Session = Depends(get_db)): 
    return author_crud.get_author_by_id(db=db, id=id)

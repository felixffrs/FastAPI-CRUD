from sqlalchemy.orm import Session
from schemas import author_schemas
from models.author import Author
from fastapi import HTTPException

def create_author(db: Session, author: author_schemas.AuthorCreate) -> Author:
    db_author = Author(name=author.name, birth_date=author.birth_date, biography=author.biography) 
    db.add(db_author)
    db.commit()
    return db_author

def get_all_authors(db: Session) -> list[Author]:
    authors = db.query(Author).all()
    return authors

def get_author_by_id(db: Session, id: int) -> Author:
    author = db.query(Author).filter(Author.id == id).first()
    if not author:
        raise HTTPException(404, {
            "message": f"Author id {id} not found"
        })
    return author

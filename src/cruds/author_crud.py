from sqlalchemy.orm import Session
from schemas import author_schemas
from models.author import Author

def create_user(db: Session, author: author_schemas.AuthorCreate):
    db_author = Author(name=author.name, birth_date=author.birth_date, biography=author.biography) 
    db.add(db_author)
    db.commit()
    return db_author

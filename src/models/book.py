from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    pages = Column(Integer, nullable=False)
    isbn_code = Column(String, nullable=False, unique=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    reviews = relationship("Review", backref="books")
    
    def __repr__(self):
        return f'Book(id={self.id}, title={self.title}, pages={self.pages}, isbn_code={self.isbn_code}, author_id={self.author_id})'


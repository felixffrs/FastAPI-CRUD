from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True)
    rating = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    
    def __repr__(self):
        return f'Review(id={self.id}, rating={self.rating}, description={self.description}, biography={self.biography}, book_id={self.book_id})'



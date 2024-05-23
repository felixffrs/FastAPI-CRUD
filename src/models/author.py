from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    biography = Column(String, nullable=False)
    books = relationship("Book", backref="authors")
    
    def __repr__(self):
        return f'Author(id={self.id}, name={self.name}, birth_date={self.birth_date}, biography={self.biography})'



from sqlalchemy import Column, Integer, String
from database import Base


class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    image_url = Column(String, index=True)

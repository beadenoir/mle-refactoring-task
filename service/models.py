from sqlalchemy import Column, Integer, Float
from database import Base

class House(Base):
    __tablename__ = "houses"
    table_id = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    bedrooms = Column(Integer)
    sqft_living = Column(Integer)
    center_distance = Column(Float)
    price = Column(Float)

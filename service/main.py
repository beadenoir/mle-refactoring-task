from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated

from models import *
from database import engine, SessionLocal
from sqlalchemy.orm import Session 



app = FastAPI() #docs_url="/"

Base.metadata.create_all(bind=engine)


# pydantic model
class Domicile(BaseModel):
    id: int
    bedrooms: int
    sqft_living: int
    center_distance: float
    price: float

    class Config:
        orm_mode = True


# connection to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    # try open database, always close no matter what


# prints basic info on localhost
@app.get("/")
def index():
    return {"data": "house list"}

@app.get("/houses",response_model=List[Domicile])
def get_all_houses(db: Session = Depends(get_db)):
    house = db.query(House).all()
    if not house:
        raise HTTPException(status_code=404, detail="house not found")
    return house


# add a house (create data)
@app.post("/houses", response_model=Domicile)  # houses beeing the tablename of the House class in models.py
def create_house(item: Domicile, db: Session = Depends(get_db)):
        new_house = House(id=item.id, bedrooms=item.bedrooms, sqft_living=item.sqft_living, center_distance=item.center_distance, price=item.price)
        db.add(new_house)
        db.commit()
        db.refresh(new_house)
        return new_house

@app.put("/houses/{table_id}")
def update_house(table_id: int, item: Domicile, db:Session = Depends(get_db)):
    house = db.query(House).filter(House.table_id == table_id)
    if not house.first():
        raise HTTPException(status_code=404, detail="house not found")
    house.update(item.dict())
    db.commit()
    return "update succesful"

@app.delete("/houses/{table_id}")
def delete(table_id: int, db: Session = Depends(get_db)):
    house = db.query(House).filter(House.table_id == table_id)
    if not house.first():
        raise HTTPException(status_code=404, detail="house not found")
    house.delete(synchronize_session=False)
    db.commit()
    return "delete successful"



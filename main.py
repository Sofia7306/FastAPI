from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine
from db import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/tracks/", response_model=schemas.TrackOut)
def create_track(track: schemas.TrackCreate, db: Session = Depends(get_db)):
    return crud.create_track(db, track)

@app.get("/tracks/", response_model=list[schemas.TrackOut])
def read_tracks(db: Session = Depends(get_db)):
    return crud.get_tracks(db)

@app.post("/users/{user_id}/like/{track_id}", response_model=schemas.UserOut)
def like_track(user_id: int, track_id: int, db: Session = Depends(get_db)):
    user = crud.like_track(db, user_id, track_id)
    if not user:
        raise HTTPException(status_code=404, detail="User or track not found")
    return user

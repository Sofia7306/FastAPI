from sqlalchemy.orm import Session
from db.models import User, Track
from db.schemas import UserCreate, TrackCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_track(db: Session, track: TrackCreate):
    db_track = Track(**track.dict())
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track

def get_tracks(db: Session):
    return db.query(Track).all()

def get_users(db: Session):
    return db.query(User).all()

def like_track(db: Session, user_id: int, track_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    track = db.query(Track).filter(Track.id == track_id).first()
    if user and track and track not in user.liked_tracks:
        user.liked_tracks.append(track)
        db.commit()
    return user

from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

user_likes = Table(
    'user_likes',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('track_id', Integer, ForeignKey('tracks.id')),
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)

    liked_tracks = relationship("Track", secondary=user_likes, back_populates="liked_by")

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artist = Column(String)
    genre = Column(String)

    liked_by = relationship("User", secondary=user_likes, back_populates="liked_tracks")

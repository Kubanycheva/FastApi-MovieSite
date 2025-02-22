from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from models import StatusChoices, TypeChoices


class UserProfileSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    phone_number: Optional[str] = None
    hashed_password: str
    age: Optional[int] = None
    status: StatusChoices

    class Config:
        orm_mode = True


class CountrySchema(BaseModel):
    id: int
    country_name: str

    class Config:
        orm_mode = True


class DirectorSchema(BaseModel):
    id: int
    director_name: str
    bio: str
    age: Optional[int] = None
    actor_image: str

    class Config:
        orm_mode = True


class GenreSchema(BaseModel):
    id: int
    genre_name: str

    class Config:
        orm_mode = True


class ActorSchema(BaseModel):
    id: int
    actor_name: str
    bio: str
    age: int
    actor_image: str

    class Config:
        orm_mode = True


class MovieSchema(BaseModel):
    id: int
    movie_name: str
    year: int
    country_ids: List[int]
    director_ids: List[int]
    actor_ids: List[int]
    genre_ids: List[int]
    description: str
    movie_trailer: str
    movie_image: str
    movie_time: int
    types: TypeChoices
    status_movie: Optional[str] = None
    status: Optional[StatusChoices] = None

    class Config:
        orm_mode = True


class MovieLanguageSchema(BaseModel):
    id: int
    language: str
    video: str
    movie: int

    class Config:
        orm_mode = True


class MomentsSchema(BaseModel):
    id: int
    movie_id: int
    moment_name: str

    class Config:
        orm_mode = True


class RatingSchema(BaseModel):
    id: int
    user: int
    movie: int
    stars: int
    text: str
    created_date: datetime

    class Config:
        orm_mode = True


class FavoriteSchema(BaseModel):
    id: int
    user: int
    created_date: datetime

    class Config:
        orm_mode = True


class FavoriteMovieSchema(BaseModel):
    id: int
    cart: int
    movie: int
    viewed_at: datetime

    class Config:
        orm_mode = True


class HistorySchema(BaseModel):
    id: int
    user: str
    movie: int
    viewed_at: datetime
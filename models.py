from sqlalchemy import String, Integer, Enum, Text, ForeignKey, Table, Column, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from typing import Optional, List
from database import Base
from enum import Enum as PyEnum


class StatusChoices(str, PyEnum):
    pro = 'pro'
    simple = 'simple'


class TypeChoices(str, PyEnum):
    p144 = '144p'
    p360 = '360p'
    p480 = '480p'
    p720 = '720p'
    p1080 = '1080p'


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    username: Mapped[str] = mapped_column(String(40), unique=True)
    phone_number: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), nullable=False, default=StatusChoices.pro)

    def set_password(self, password: str):
        self.hashed_password = bcrypt.hash(password)

    def check_password(self, password: str):
        return bcrypt.verify(password, self.hashed_password)


class Country(Base):
    __tablename__ = 'country'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    country_name: Mapped[str] = mapped_column(String(32), unique=True)

    movies: Mapped[List['Movie']] = relationship(
        "Movie",
        secondary='movie_country_association',
        back_populates="countries"  # Исправлено на 'countries'
    )


class Director(Base):
    __tablename__ = 'director'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    director_name: Mapped[str] = mapped_column(String(32))
    bio: Mapped[str] = mapped_column(Text)
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    actor_image: Mapped[str] = mapped_column(String)

    movies: Mapped[List['Movie']] = relationship(
        "Movie",
        secondary='movie_director_association',
        back_populates="directors"
    )


class Genre(Base):
    __tablename__ = 'genre'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    genre_name: Mapped[str] = mapped_column(String(32), unique=True)

    movies: Mapped[List['Movie']] = relationship(
        "Movie",
        secondary='movie_genre_association',
        back_populates="genres"
    )


class Actor(Base):
    __tablename__ = 'actor'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    actor_name: Mapped[str] = mapped_column(String(32))
    bio: Mapped[str] = mapped_column(Text)
    age: Mapped[int] = mapped_column(Integer)
    actor_image: Mapped[str] = mapped_column(String)

    movies: Mapped[List['Movie']] = relationship(
        "Movie",
        secondary='movie_actor_association',
        back_populates="actors"
    )


movie_country_association = Table(
    'movie_country_association',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id')),
    Column('country_id', ForeignKey('country.id'))
)

movie_director_association = Table(
    'movie_director_association',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id')),
    Column('director_id', ForeignKey('director.id'))
)

movie_actor_association = Table(
    'movie_actor_association',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id')),
    Column('actor_id', ForeignKey('actor.id'))
)

movie_genre_association = Table(
    'movie_genre_association',
    Base.metadata,
    Column('movie_id', ForeignKey('movie.id')),
    Column('genre_id', ForeignKey('genre.id'))
)


class Movie(Base):
    __tablename__ = 'movie'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    movie_name: Mapped[str] = mapped_column(String(32), unique=True)
    year: Mapped[int] = mapped_column(Integer)

    countries: Mapped[List[Country]] = relationship(
        'Country',
        secondary=movie_country_association,
        back_populates='movies'
    )
    directors: Mapped[List[Director]] = relationship(
        "Director",
        secondary=movie_director_association,
        back_populates="movies"
    )
    actors: Mapped[List[Actor]] = relationship(
        "Actor",
        secondary=movie_actor_association,
        back_populates="movies"
    )
    genres: Mapped[List[Genre]] = relationship(
        "Genre",
        secondary=movie_genre_association,
        back_populates="movies"
    )

    types: Mapped[str] = mapped_column(String(255), nullable=False, default="")

    def set_types(self, types: List[TypeChoices]):
        self.types = ','.join([type_choice.value for type_choice in types])

    def get_types(self) -> List[TypeChoices]:
        return [TypeChoices(type_str) for type_str in self.types.split(',')] if self.types else []

    movie_time: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(Text)
    movie_trailer: Mapped[str] = mapped_column(String)
    movie_image: Mapped[str] = mapped_column(String)
    status_movie: Mapped[str] = mapped_column(String(16), nullable=True)
    status: Mapped[StatusChoices] = mapped_column(Enum(StatusChoices), nullable=False, default=StatusChoices.pro)


class MovieLanguages(Base):
    __tablename__ = 'movie_languages'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    language: Mapped[str] = mapped_column(String(15), nullable=True)
    video: Mapped[str] = mapped_column(String)
    movie: Mapped[int] = mapped_column(ForeignKey('movie.id'))


class Moments(Base):
    __tablename__ = 'moments'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, index=True, primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey('movie.id'))
    moment_name: Mapped[str] = mapped_column(String)


class Rating(Base):
    __tablename__ = 'rating'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, index=True, primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))
    movie: Mapped[int] = mapped_column(ForeignKey('movie.id'))
    stars: Mapped[int] = mapped_column(Integer)
    text: Mapped[str] = mapped_column(Text)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Favorite(Base):
    __tablename__ = 'favorite'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, index=True, primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class FavoriteMovie(Base):
    __tablename__ = 'favorite_movie'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, index=True, primary_key=True)
    cart: Mapped[int] = mapped_column(ForeignKey('favorite.id'))
    movie: Mapped[int] = mapped_column(ForeignKey('movie.id'))


class History(Base):
    __tablename__ = 'history'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))
    movie: Mapped[int] = mapped_column(ForeignKey('movie.id'))
    viewed_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
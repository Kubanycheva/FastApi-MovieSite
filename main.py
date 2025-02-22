import fastapi
from models import (UserProfile, Country, Director, Genre, Actor, Movie,
                    MovieLanguages, Moments,Rating, FavoriteMovie, History, TypeChoices)
from schema import (UserProfileSchema, CountrySchema, DirectorSchema, GenreSchema, ActorSchema, MovieSchema,
                    MovieLanguageSchema, MomentsSchema, RatingSchema, FavoriteMovieSchema, HistorySchema)
from database import SessionLocal, engine
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from schema import *
from fastapi import FastAPI
from admin_views import create_admin
from typing import List, Optional

from config import (SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE, ALGORITHM)
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime

movie_app = fastapi.FastAPI(title='Movie-Site')

create_admin(movie_app)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@movie_app.post('/country/create', response_model=CountrySchema, tags=['Country'])
async def create_country(country: CountrySchema, db: Session = Depends(get_db)):
    db_country = Country(country_name=country.country_name)
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


@movie_app.get('/country/', response_model=List[CountrySchema], tags=['Country'])
async def list_country(db: Session = Depends(get_db)):
    return db.query(Country).all()


@movie_app.get('/country/{country_id}/', response_model=CountrySchema, tags=['Country'])
async def detail_country(country_id: int, db: Session = Depends(get_db)):
    country = db.query(Country).filter(Country.id == country_id).first()
    if country is None:
        raise HTTPException(status_code=404, detail='Country Not Found')
    return country


@movie_app.put('/country/update', response_model=CountrySchema, tags=['Country'])
async def update_country(country_id: int, country_data: CountrySchema,
                         db: Session = Depends(get_db)):
    country = db.query(Country).filter(Country.id == country_id).first()
    if country is None:
        raise HTTPException(status_code=404, detail='Country Not Found')
    db.commit()
    db.refresh(country)
    return country


@movie_app.delete('/country/delete', tags=['Country'])
async def delete_country(country_id: int, db: Session = Depends(get_db)):
    return db.query(Country).all()


@movie_app.post('/director/create', response_model=DirectorSchema, tags=['Director'])
async def create_director(director: DirectorSchema, db: Session = Depends(get_db)):
    db_director = Director(**director.dict())
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director


@movie_app.get('/director', response_model=List[DirectorSchema], tags=['Director'])
async def list_director(db: Session = Depends(get_db)):
    return db.query(Director).all()


@movie_app.get('/director/{director_id}', response_model=DirectorSchema, tags=['Director'])
async def detail_director(director_id: int, db: Session = Depends(get_db)):
    director =db.query(Director).filter(Director.id == director_id).first()
    if director is None:
        raise HTTPException(status_code=404, detail='Director Not Found')
    return director


@movie_app.put('/director/update', response_model=DirectorSchema, tags=['Director'])
async def update_director(director_id: int, director_data: DirectorSchema, db: Session = Depends(get_db)):
    director = db.query(Director).filter(Director.id == director_id).first()
    if director is None:
        raise HTTPException(status_code=404, detail='Director Not Found')
    return director

    for director_key,director_value in director_data.dict().items():
        setattr(director, director_key, director_value)
    db.commit()
    db.refresh(director)
    return director


@movie_app.delete('/director.delete', tags=['Director'])
async def delete_director(director_id: int, db: Session = Depends(get_db)):
    director = db.query(Director).filter(Director.id == director_id).first()
    if director is None:
        raise HTTPException(status_code=404, detail='Director Not Found')
    db.delete(director)
    return {'message': 'This director is deleted'}


@movie_app.post('/genre/create', response_model=GenreSchema, tags=['Genre'])
async def create_genre(genre: GenreSchema, db: Session = Depends(get_db)):
    db_genre = Genre(genre_name=genre.genre_name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


@movie_app.get('/genre', response_model=List[GenreSchema], tags=['Genre'])
async def list_genre(db: Session = Depends(get_db)):
    return db.query(Genre).all()


@movie_app.get('/genre/{genre_id/', response_model=GenreSchema, tags=['Genre'])
async def detail_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre is None:
        raise HTTPException(status_code=404, detail='Genre Not Found')
    return genre


@movie_app.put('/genre/update', response_model=GenreSchema, tags=['Genre'])
async def update_genre(genre_id: int, genre_data: GenreSchema, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre is None:
        raise HTTPException(status_code=404, detail='Genre Not Found')
    genre.genre_name = genre_data.genre_name
    db.commit()
    db.refresh(genre)
    return genre


@movie_app.delete('/genre/{genre_id}', tags=['Genre'])
async def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if genre is None:
        raise HTTPException(status_code=404, detail='Genre Not Found')
    db.delete(genre)
    db.commit()
    return {'message': 'This genre is deleted'}


@movie_app.post('/actor/create', response_model=ActorSchema, tags=['Actor'])
async def create_actor(actor: ActorSchema, db: Session = Depends(get_db)):
    db_actor = Actor(**actor.dict())
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


@movie_app.get('/actor', response_model=List[ActorSchema], tags=['Actor'])
async def list_actor(db: Session = Depends(get_db)):
    return db.query(Actor).all()


@movie_app.get('/actor/{actor_id}', response_model=ActorSchema, tags=['Actor'])
async def detail_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail='Actor Not Found')
    return actor


@movie_app.put('/actor/update', response_model=ActorSchema, tags=['Actor'])
async def update_actor(actor_id: int, actor_data: ActorSchema, db: Session = Depends(get_db)):
    actor = db.query(Actor).filter(Actor.id == actor_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail='Actor Not Found')
    return actor

    for actor_key, actor_value in actor_data.dict().items():
        setattr(actor, actor_key, actor_value)
    db.commit()
    db.refresh(actor)
    return actor


@movie_app.delete('/actor/delete', tags=['Actor'])
async def delete_actor(actr_id: int, db: Session = Depends(get_db)):
    actor = db.query(Actor).filter(Actor.id == actr_id).first()
    if actor is None:
        raise HTTPException(status_code=404, detail='Actor Not Found')
    db.delete(actor)
    db.commit()
    return {'message': 'This actor is deleted'}


@movie_app.post('/movie/create', response_model=MovieSchema, tags=['Movie'])
async def create_movie(movie: MovieSchema, db: Session = Depends(get_db)):
    countries = db.query(Country).filter(Country.id.in_(movie.country_ids)).all()
    directors = db.query(Director).filter(Director.id.in_(movie.director_ids)).all()
    actors = db.query(Actor).filter(Actor.id.in_(movie.actor_ids)).all()
    genres = db.query(Genre).filter(Genre.id.in_(movie.genre_ids)).all()

    db_movie = Movie(
        id=movie.id,
        movie_name=movie.movie_name,
        year=movie.year,
        countries=countries,
        directors=directors,
        actors=actors,
        genres=genres,
        description=movie.description,
        movie_trailer=movie.movie_trailer,
        movie_image=movie.movie_image,
        movie_time=movie.movie_time,
        types=movie.types.value,
        status_movie=movie.status_movie or 'default_value',
        status=movie.status
    )

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie


@movie_app.get('movie', response_model=MovieSchema, tags=['Movie'])
async def list_movie(db: Session = Depends(get_db)):
    return db.query(Movie).all()


@movie_app.get('movie/{movie_id}', response_model=MovieSchema, tags=['Movie'])
async def detail_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail='Movie Not Found')
    return movie


@movie_app.put('/movie/update', response_model=MovieSchema, tags=['Movie'])
async def update_movie(movie_id: int, movie_data: MovieSchema, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail='Movie Not Found')
    return movie

    for movie_key, movie_value in movie_data.dict().items():
        setattr(movie, movie_key, movie_value)
    db.commit()
    db.refresh(movie)
    return movie


@movie_app.delete('/movie/delete', tags=['Movie'])
async def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail='Movie Not Found')
    return movie
    db.delete(movie)
    db.commit()
    return {'message': 'This movie is deleted'}


@movie_app.post('/languages/create', response_model=MovieLanguageSchema, tags=['MovieLanguages'])
async def create_languages(languages: MovieLanguageSchema, db: Session = Depends(get_db)):
    db_languages = MovieLanguages(**languages.dict())
    db.add(db_languages)
    db.commit()
    db.refresh(db_languages)
    return db_languages


@movie_app.get('/languages', response_model=MovieLanguageSchema, tags=['MovieLanguages'])
async def list_languages(db: Session = Depends(get_db)):
    return db.query(MovieLanguages).all()


@movie_app.get('/languages/{languages_id}', response_model=MovieLanguageSchema, tags=['MovieLanguages'])
async def detail_languages(languages_id: int, db: Session = Depends(get_db)):
    languages = db.query(MovieLanguages).filter(MovieLanguages.id == languages_id).first()
    if languages is None:
        raise HTTPException(status_code=404, detail='Not found')
    return languages


@movie_app.put('/languages/update', response_model=MovieLanguageSchema, tags=['MovieLanguages'])
async def update_languages(languages_id: int, languages_data: MovieLanguageSchema, db: Session = Depends(get_db)):
    languages = db.query(MovieLanguages).filter(MovieLanguages.id == languages_id).first()
    if languages is None:
        raise HTTPException(status_code=404, detail='Not found')
    return languages

    for laguages_key, languages_value in languages_data.dict().items():
        setattr(languages, languages_key, languages_value)
    db.commit()
    db.refresh(languages)
    return languages


@movie_app.delete('/languages/delete', tags=['MovieLanguages'])
async def delete_languages(languages_id: int, db: Session = Depends(get_db)):
    languages = db.query(MovieLanguages).filter(MovieLanguages.id == languages_id).first()
    if languages is None:
        raise HTTPException(status_code=404, detail='Not found')
    db.delete(languages)
    db.commit()
    return{'message': 'This success is deleted'}


@movie_app.post('/moments/create', response_model=MomentsSchema, tags=['Moments'])
async def create_moments(moments: MomentsSchema,  db: Session = Depends(get_db)):
    db_moments = Moments(moment_name=moments.moment_name)
    db.add(db_moments)
    db.commit()
    db.refresh(db_moments)
    return db_moments


@movie_app.get('/moments', response_model=MomentsSchema, tags=['Moments'])
async def list_moments(db: Session = Depends(get_db)):
    return db.query(Moments).all()


@movie_app.get('/moments/{moments_id}', response_model=MomentsSchema, tags=['Moments'])
async def detail_moments(moments_id: int,  db: Session = Depends(get_db)):
    moments = db.query(Moments).filter(Moments.id==moments_id).first()
    if moments is None:
        raise HTTPException(status_code=404, detail='Moments Not Found')
    return moments


@movie_app.put('/moments/update', response_model=MomentsSchema, tags=['Moments'])
async def update_moments(moments_id: int, moments_data: MomentsSchema,  db: Session = Depends(get_db)):
    moments = db.query(Moments).filter(Moments==moments_id).first()
    if moments is None:
        raise HTTPException(status_code=404, detail='Moments Not Found')
    moments.movie_moments=moments_data.movie_moments
    db.commit()
    db.refresh(moments)
    return moments


@movie_app.delete('/moments/delete', tags=['Moments'])
async def delete_moments(moments_id: int, db: Session = Depends(get_db)):
    moments = db.query(Moments).filter(Moments.id == moments_id).first()
    if moments is None:
        raise HTTPException(status_code=404, detail='Moments Not Found')
    db.delete(moments)
    db.commit()
    return {'message': 'This moments is deleted'}








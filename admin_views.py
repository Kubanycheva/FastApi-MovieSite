from sqladmin import Admin, ModelView
from models import UserProfile, Country, Director, Genre, Actor, Movie
from database import engine


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.username, UserProfile.status]
    name = 'User'
    name_plural = 'Users'


class CountryAdmin(ModelView, model=Country):
    column_list = [Country.id, Country.country_name]
    name = 'Country'
    name_plural = 'Countries'


class DirectorAdmin(ModelView, model=Director):
    column_list = [Director.id, Director.director_name]
    name = 'Director'
    name_plural = 'Directors'


class GenreAdmin(ModelView, model=Genre):
    column_list = [Genre.id, Genre.genre_name]
    name = 'Genre'
    name_plural = 'Genres'


class ActorAdmin(ModelView, model=Actor):
    column_list = [Actor.id, Actor.actor_name]
    name = 'Actor'
    name_plural = 'Actors'


class MovieAdmin(ModelView, model=Movie):
    column_list = [Movie.id, Movie.movie_name]
    name = 'Movie'
    name_plural = 'Movies'


def create_admin(movie_app):
    admin = Admin(movie_app, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CountryAdmin)
    admin.add_view(DirectorAdmin)
    admin.add_view(GenreAdmin)
    admin.add_view(ActorAdmin)
    admin.add_view(MovieAdmin)

    return admin
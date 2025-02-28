from sqladmin import Admin, ModelView
from models import (UserProfile, Country, Director,
                    Genre, Actor, Movie, MovieLanguages, Moments, Rating, Favorite, FavoriteMovie, History)
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


class MovieLanguagesAdmin(ModelView, model=MovieLanguages):
    column_list = [MovieLanguages.id, MovieLanguages.language]
    name = 'MovieLanguage'
    name_plural = 'MovieLanguages'


class MomentsAdmin(ModelView, model=Moments):
    column_list = [Moments.id, Moments.moment_name]
    name = 'Moment'
    name_plural = 'Moments'


class RatingAdmin(ModelView, model=Rating):
    column_list = [Rating.id, Rating.created_date]
    name = 'Rating'
    name_plural = 'Ratings'


class FavoriteAdmin(ModelView, model=Favorite):
    column_list = [Favorite.id, Favorite.created_date]
    name = 'Favorite'
    name_plural = 'Favorites'


class FavoriteMovieAdmin(ModelView, model=FavoriteMovie):
    column_list = [FavoriteMovie.id]
    name = 'FavoriteMovie'
    name_plural = 'FavoriteMovies'


class HistoryAdmin(ModelView, model=History):
    column_list = [History.id]
    name = 'History'
    name_plural = 'Histories'


def create_admin(movie_app):
    admin = Admin(movie_app, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CountryAdmin)
    admin.add_view(DirectorAdmin)
    admin.add_view(GenreAdmin)
    admin.add_view(ActorAdmin)
    admin.add_view(MovieAdmin)
    admin.add_view(MovieLanguagesAdmin)
    admin.add_view(MomentsAdmin)
    admin.add_view(RatingAdmin)
    admin.add_view(FavoriteAdmin)
    admin.add_view(FavoriteMovieAdmin)
    admin.add_view(HistoryAdmin)

    return admin
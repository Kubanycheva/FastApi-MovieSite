"""empty message

Revision ID: 261e2cff7216
Revises: 
Create Date: 2025-02-22 20:50:56.447837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '261e2cff7216'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('actor_name', sa.String(length=32), nullable=False),
    sa.Column('bio', sa.Text(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('actor_image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_actor_id'), 'actor', ['id'], unique=False)
    op.create_table('country',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('country_name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('country_name')
    )
    op.create_index(op.f('ix_country_id'), 'country', ['id'], unique=False)
    op.create_table('director',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('director_name', sa.String(length=32), nullable=False),
    sa.Column('bio', sa.Text(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('actor_image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_director_id'), 'director', ['id'], unique=False)
    op.create_table('genre',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('genre_name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('genre_name')
    )
    op.create_index(op.f('ix_genre_id'), 'genre', ['id'], unique=False)
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('movie_name', sa.String(length=32), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('types', sa.String(length=255), nullable=False),
    sa.Column('movie_time', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('movie_trailer', sa.String(), nullable=False),
    sa.Column('movie_image', sa.String(), nullable=False),
    sa.Column('status_movie', sa.String(length=16), nullable=True),
    sa.Column('status', sa.Enum('pro', 'simple', name='statuschoices'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('movie_name')
    )
    op.create_index(op.f('ix_movie_id'), 'movie', ['id'], unique=False)
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=False),
    sa.Column('last_name', sa.String(length=40), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('pro', 'simple', name='statuschoices'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_user_profile_id'), 'user_profile', ['id'], unique=False)
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_favorite_id'), 'favorite', ['id'], unique=False)
    op.create_table('history',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('movie', sa.Integer(), nullable=False),
    sa.Column('viewed_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['movie'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('moments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('moment_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_moments_id'), 'moments', ['id'], unique=False)
    op.create_table('movie_actor_association',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('actor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['actor_id'], ['actor.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'actor_id')
    )
    op.create_table('movie_country_association',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'country_id')
    )
    op.create_table('movie_director_association',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['director_id'], ['director.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'director_id')
    )
    op.create_table('movie_genre_association',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('movie_id', 'genre_id')
    )
    op.create_table('movie_languages',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('language', sa.String(length=15), nullable=True),
    sa.Column('video', sa.String(), nullable=False),
    sa.Column('movie', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_movie_languages_id'), 'movie_languages', ['id'], unique=False)
    op.create_table('rating',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('movie', sa.Integer(), nullable=False),
    sa.Column('stars', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['movie'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user'], ['user_profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rating_id'), 'rating', ['id'], unique=False)
    op.create_table('favorite_movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cart', sa.Integer(), nullable=False),
    sa.Column('movie', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart'], ['favorite.id'], ),
    sa.ForeignKeyConstraint(['movie'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_favorite_movie_id'), 'favorite_movie', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_favorite_movie_id'), table_name='favorite_movie')
    op.drop_table('favorite_movie')
    op.drop_index(op.f('ix_rating_id'), table_name='rating')
    op.drop_table('rating')
    op.drop_index(op.f('ix_movie_languages_id'), table_name='movie_languages')
    op.drop_table('movie_languages')
    op.drop_table('movie_genre_association')
    op.drop_table('movie_director_association')
    op.drop_table('movie_country_association')
    op.drop_table('movie_actor_association')
    op.drop_index(op.f('ix_moments_id'), table_name='moments')
    op.drop_table('moments')
    op.drop_table('history')
    op.drop_index(op.f('ix_favorite_id'), table_name='favorite')
    op.drop_table('favorite')
    op.drop_index(op.f('ix_user_profile_id'), table_name='user_profile')
    op.drop_table('user_profile')
    op.drop_index(op.f('ix_movie_id'), table_name='movie')
    op.drop_table('movie')
    op.drop_index(op.f('ix_genre_id'), table_name='genre')
    op.drop_table('genre')
    op.drop_index(op.f('ix_director_id'), table_name='director')
    op.drop_table('director')
    op.drop_index(op.f('ix_country_id'), table_name='country')
    op.drop_table('country')
    op.drop_index(op.f('ix_actor_id'), table_name='actor')
    op.drop_table('actor')
    # ### end Alembic commands ###

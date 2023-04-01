from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username, age):
        user = self.__find_user_by_username(username)
        if user:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        if not self.__find_user_by_username(username):
            raise Exception('This user does not exist!')

        if self.__find_movie_by_title(movie.title):
            raise Exception('Movie already added to the collection!')

        if not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        self.movies_collection.append(movie)
        for user in self.users_collection:
            if username == user.username:
                user.movies_owned.append(movie)
                return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username, movie, **kwargs):
        if not self.__find_movie_by_title(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)

        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username, movie):
        if not self.__find_movie_by_title(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')

        if not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        self.movies_collection.remove(movie)
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.remove(movie)
                return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username, movie):
        if username == movie.owner.username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')
        elif self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} already liked the movie {movie.title}!')
        else:
            movie.likes += 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.append(movie)
            return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username, movie):
        if not self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        else:
            movie.likes -= 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.pop(user.movies_liked.index(movie))
            return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())

            return '\n'.join(result_str)

    def __str__(self):

        if len(self.users_collection) == 0:
            users = "No users."
        else:
            users = ', '.join(u.username for u in self.users_collection)

        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join(m.title for m in self.movies_collection)

        return f'All users: {users}\nAll movies: {movies}'

    def __find_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def __find_movie_by_title(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False

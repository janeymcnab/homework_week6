from src.movie import Movie


class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []

    def add_favourite(self, movie):
        self.favourites.append(movie)
        return len(self.favourites)


    def remove_favourite(self, movie):
        if movie.title == movie:
            self.favourites.remove(movie)
        return len(self.favourites)

    def return_favourites_list(self):
        return self.favourites
from dao.model.movie import Movie

class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, value):
        return self.session.query(Movie).filter(Movie.director_id == value).all()

    def get_by_genre_id(self, value):
        return self.session.query(Movie).filter(Movie.genre_id == value).all()

    def get_by_year(self, value):
        return self.session.query(Movie).filter(Movie.year == value).all()

    def create(self, movie_dict):
        m_create = Movie(**movie_dict)
        self.session.add(m_create)
        self.session.commit()

    def update(self, movie_dict):
        movie = self.get_one(movie_dict.get('id'))
        movie.title = movie_dict.get('title')
        movie.description = movie_dict.get('description')
        movie.trailer = movie_dict.get('trailer')
        movie.year = movie_dict.get('year')
        movie.rating = movie_dict.get('rating')
        movie.genre_id = movie_dict.get('genre_id')
        movie.director_id = movie_dict.get('director_id')

        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

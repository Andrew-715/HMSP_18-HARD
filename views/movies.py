from flask_restx import Resource, Namespace
from flask import request

from dao.model.movie import MovieSchema
from implemented import movie_service


movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')

        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year
        }

        all_movies = movie_service.get_all(filters)
        result = movies_schema.dump(all_movies)
        return result, 200

    def post(self):
        req_json = request.json
        new_movie = movie_service(**req_json)
        return 'Movie added', 201, {'location': f'/movies/{new_movie.id}'}

@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid:int):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200

        except Exception as e:
            return str(e), 404

    def put(self, mid:int):
        req_json = request.json

        if 'id' not in req_json:
            req_json['id'] = mid

        movie_service.update(req_json)
        return 'Movie updated', 204

    def delete(self, mid:int):
        movie_service.delete(mid)
        return 'Movie deleted', 204

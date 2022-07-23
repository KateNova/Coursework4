from typing import Dict, Tuple, Any, List
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema, Movie
from decorator import auth_required, admin_required
from implemented import movie_service

movie_ns = Namespace('movies')

# создаем экземпляры класса GenreSchema
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self) -> Tuple[List[Dict[str, Any]], int]:

        filters: Dict[str, str] = {
            "director_id": request.args.get("director_id"),
            "genre_id": request.args.get("genre_id"),
            "year": request.args.get("year"),
        }

        all_movies: List[Movie] = movie_service.get_all(filters)
        return movies_schema.dump(all_movies), 200

    @admin_required
    def post(self) -> Tuple[str, int, Dict[str, str]]:
        req_json: Dict[str, Any] = request.json
        movie: Movie = movie_service.create(req_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    @auth_required
    def get(self, mid: int) -> Tuple[Dict[str, Any], int]:
        movie: Movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, mid: int) -> Tuple[str, int]:
        req_json: Dict[str, Any] = request.json
        movie_service.update(mid, req_json)
        return "", 204

    @admin_required
    def delete(self, mid: int) -> Tuple[str, int]:
        movie_service.delete(mid)
        return "", 204

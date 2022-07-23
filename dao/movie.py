from typing import List

from sqlalchemy.orm import scoped_session

from dao.model.movie import Movie


class MovieDAO:
    session: scoped_session

    def __init__(self, session: scoped_session) -> None:
        self.session = session

    def get_one(self, mid: int) -> Movie:
        return self.session.query(Movie).get(mid)

    def get_all(self) -> List[Movie]:
        return self.session.query(Movie).all()

    def get_by_director_id(self, val: int) -> List[Movie]:
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val: int) -> List[Movie]:
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val: int) -> List[Movie]:
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie: Movie) -> Movie:
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid: int) -> None:
        movie: Movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie: Movie) -> Movie:
        self.session.add(movie)
        self.session.commit()
        return movie

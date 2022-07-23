from typing import List

from sqlalchemy.orm import scoped_session

from dao.model.genre import Genre


class GenreDAO:
    session: scoped_session

    def __init__(self, session: scoped_session) -> None:
        self.session = session

    def get_one(self, gid: int) -> Genre:
        return self.session.query(Genre).get(gid)

    def get_all(self) -> List[Genre]:
        return self.session.query(Genre).all()

    def create(self, genre: Genre) -> Genre:
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, genre: Genre) -> Genre:
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, gid: int) -> None:
        genre: Genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

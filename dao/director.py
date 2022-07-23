from typing import List

from sqlalchemy.orm import scoped_session

from dao.model.director import Director


class DirectorDAO:
    session: scoped_session

    def __init__(self, session: scoped_session) -> None:
        self.session = session

    def get_one(self, did: int) -> Director:
        return self.session.query(Director).get(did)

    def get_all(self) -> List[Director]:
        return self.session.query(Director).all()

    def create(self, director: Director) -> Director:
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did: int) -> None:
        director: Director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director: Director) -> Director:
        self.session.add(director)
        self.session.commit()
        return director

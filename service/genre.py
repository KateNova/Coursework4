from typing import Dict, Any, List

from dao.genre import GenreDAO
from dao.model.genre import Genre


class GenreService:
    dao: GenreDAO

    def __init__(self, dao: GenreDAO) -> None:
        self.dao = dao

    def get_one(self, gid: int) -> Genre:
        return self.dao.get_one(gid)

    def get_all(self) -> List[Genre]:
        return self.dao.get_all()

    def create(self, genre_d: Dict[str, Any]) -> Genre:
        genre: Genre = Genre(**genre_d)
        return self.dao.create(genre)

    def update(self, genre_id: int, genre_d: Dict[str, Any]) -> Genre:
        genre_by_id: Genre = self.dao.get_one(genre_id)
        for k, v in genre_d.items():
            setattr(genre_by_id, k, v)
        return self.dao.update(genre_by_id)

    def partially_update(self, genre_id: int, genre_d: Dict[str, Any]) -> Genre:
        genre_by_id: Genre = self.dao.get_one(genre_id)
        if "name" in genre_d:
            genre_by_id.name = genre_d.get("name")
        self.dao.update(genre_by_id)

    def delete(self, gid: int) -> None:
        self.dao.delete(gid)

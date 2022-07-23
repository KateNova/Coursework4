from typing import List, Dict, Any

from dao.director import DirectorDAO

from dao.model.director import Director


class DirectorService:
    dao: DirectorDAO

    def __init__(self, dao: DirectorDAO) -> None:
        self.dao = dao

    def get_one(self, did: int) -> Director:
        return self.dao.get_one(did)

    def get_all(self) -> List[Director]:
        return self.dao.get_all()

    def create(self, director_d: Dict[str, Any]) -> Director:
        director: Director = Director(**director_d)
        return self.dao.create(director)

    def update(self, director_id: int, director_d: Dict[str, Any]):
        director_by_id: Director = self.dao.get_one(director_id)
        for k, v in director_d.items():
            setattr(director_by_id, k, v)
        return self.dao.update(director_by_id)

    def partially_update(self, director_id: int, director_d: Dict[str, Any]):
        director_by_id: Director = self.dao.get_one(director_id)
        if "name" in director_d:
            director_by_id.name = director_d.get("name")
        return self.dao.update(director_by_id)

    def delete(self, did: int) -> None:
        self.dao.delete(did)

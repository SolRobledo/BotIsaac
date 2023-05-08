import re
from typing import Optional

from src.db.mongo_O import Mongo
from src.parametros import Types


class Queries:
    def __init__(self):
        self.mongo: Mongo = Mongo()

    def get_item(self, param: str, type_: Types) -> Optional[dict]:
        query: dict = {"name": re.compile(f"^{param}$", re.IGNORECASE), "type": re.compile(type_, re.IGNORECASE)}
        data: dict = self.mongo.db["AllItems"].find_one(query)
        if not data:
            return None
        else:
            return data

    def get_card(self, param: str, type_: Types) -> Optional[dict]:
        query: dict = {"name": re.compile(param, re.IGNORECASE), "type": re.compile(type_, re.IGNORECASE)}
        data: dict = self.mongo.db["AllItems"].find_one(query)
        if not data:
            return None
        else:
            return data

    def get_r_items(self, param: str) -> Optional[list[dict]]:
        query: dict = {"name": re.compile(param, re.IGNORECASE)}
        data: list = list(self.mongo.db["AllItems"].find(query))
        if not data:
            return None
        else:
            return data

    def get_link(self, param: str, type_: Types) -> Optional[dict]:
        query: dict = {"name": re.compile(f"^{param}$", re.IGNORECASE), "type": type_}
        data: dict = self.mongo.db["AllLinks"].find_one(query)
        if not data:
            return None
        else:
            return data

    def get_link_by_id(self, param: int, type_: Types) -> Optional[dict]:
        query: dict = {"id": param, "type": type_}
        data: dict = self.mongo.db["AllLinks"].find_one(query)
        if not data:
            return None
        else:
            return data

    def get_transformation(self, param: str, type_: Types) -> Optional[dict]:
        query: dict = {"name": re.compile(f"^{param}$", re.IGNORECASE), "type": type_}
        data: dict = self.mongo.db["Transformations"].find_one(query)
        if not data:
            return None
        else:
            return data

    def get_transformations(self,) -> Optional[list[dict]]:
        query: dict = {"type": "Transformation"}
        data: list = list(self.mongo.db["Transformations"].find(query))
        if not data:
            return None
        else:
            return data


if __name__ == '__main__':
    ola = Queries()

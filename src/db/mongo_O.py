import hashlib
import json
import os

from pymongo import MongoClient
from pymongo.errors import BulkWriteError

from dotenv import load_dotenv


class Mongo:
    def __init__(self):
        load_dotenv()
        self.user: str = os.getenv("DB_USER")
        self.password: str = os.getenv("PASSWORD")
        self.ip: str = os.getenv("IP")
        self.port: str = os.getenv("PORT")
        self.client: MongoClient = MongoClient(f"mongodb://{self.user}:{self.password}@{self.ip}:{self.port}")
        self.db = self.client["Isaac_db"]

    def insert_data(self, collection: str, items: list):
        try:
            self.db[collection].insert_many(self.combine(items), ordered=False)
        except BulkWriteError:
            pass

    @staticmethod
    def combine(list_: list[dict]):
        lista: list[dict] = []
        for i in list_:
            i["_id"] = hashlib.md5(json.dumps(i, sort_keys=True).encode("utf-8")).hexdigest()
            lista.append(i)
        return lista


if __name__ == '__main__':
    ola = Mongo()

from django.conf import settings
from pymongo import MongoClient
from pymongo.synchronous.database import Database

from common.singleton import SingletonMeta


class MongoConnection(metaclass=SingletonMeta):
    """This is a class which should be used to retrieve MongoDB client.

    It serves as the only entrypoint to MongoDB. It is needed to make customizations easier in the future.
    """

    _client: MongoClient
    _db: Database

    def __init__(self):
        self._client = MongoClient(settings.MONGO_CONNECTION_STRING)
        self._db = self._client[settings.MONGO_DB_NAME]

    @property
    def client(self) -> MongoClient:
        return self._client

    @property
    def db(self) -> Database:
        return self._db

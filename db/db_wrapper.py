import psycopg2

from typing import Optional
from setup import POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER


class DBWrapper:

    def __init__(self):
        self.connection = self._db_connect()

    @staticmethod
    def _db_connect():
        return psycopg2.connect(
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host="db",
            port="5432"
        )

    def select_data_from_db(self, query_path: Optional = None):
        cur = self.connection.cursor()
        with open(query_path) as q1:
            query: str = q1.read()
        cur.execute(query)
        result = cur.fetchall()
        return result

    def insert_data_to_db(self, data):
        cur = self.connection.cursor()
        res = [photo.to_dictionary() for photo in data]
        with open('db/insert_photos.sql') as q1:
            insert_photo: str = q1.read()
        cur.executemany(insert_photo, res)
        self.connection.commit()

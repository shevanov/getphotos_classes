import psycopg2

from typing import Optional
from setup import POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER


class DBWrapper:

    def __init__(self):
        self.connection = self._db_connect()
        self.create_db()

    @staticmethod
    def _db_connect():
        return psycopg2.connect(
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            # host="db",
            host="localhost",
            port="5432"
        )

    def create_db(self):
        cur = self.connection.cursor()
        with open('../db/create_db.sql') as q1:
            create: str = q1.read()
        cur.execute(create)
        self.connection.commit()

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
        with open('./db/insert_photos.sql') as q1:
            insert_photo: str = q1.read()
        cur.executemany(insert_photo, res)
        self.connection.commit()

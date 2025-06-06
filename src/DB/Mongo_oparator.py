import pymongo
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os


load_dotenv()


class MongoOperator:
    def __init__(self, host="localhost", db_name="Curriculo"):
        self.host = host
        self.db_name = db_name

    def open_connection(self):
        self.client = pymongo.MongoClient(self.host, server_api=ServerApi("1"))

    def close_connection(self):
        self.client.close()

    def check_connection(self):
        try:
            self.open_connection()
            self.client.admin.command("ping")
            self.close_connection()
            return True
        except pymongo.errors.ConnectionFailure:
            return False

    def insert_one(self, collection_name, document):
        self.open_connection()
        db = self.client[self.db_name]
        collection = db[collection_name]
        return collection.insert_one(document)

    def find_all(self, collection_name):
        try:
            self.open_connection()
            db = self.client[self.db_name]
            collection = db[collection_name]
            results = collection.find({})
            return list(results)
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            self.close_connection()

    def find_by_query(self, collection_name, query=None):
        try:
            self.open_connection()
            db = self.client[self.db_name]
            collection = db[collection_name]
            if query is None:
                query = {}
            results = collection.find(query)
            return list(results)
        except pymongo.errors.PyMongoError as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            self.close_connection()

    def update_one(self, collection_name, query, update):
        collection = self.db[collection_name]
        return collection.update_one(query, update)

    def delete_one(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query)

    def close(self):
        self.client.close()

'''handles connectivity to/from the db'''
from pymongo import MongoClient
import random_data_gen as rdg

CONNECTION_STRING = "mongodb://docker:mongopw@localhost:55000"


def populate_mongo(count: int):
    def get_database():
        CONNECTION_STRING = "mongodb://docker:mongopw@localhost:55000"
        client = MongoClient(CONNECTION_STRING)
        return client['SCV']

    # This is added so that many files can reuse the function get_database()
    if __name__ == "__main__":
        # Get the database
        dbname = get_database()

    collection = dbname["scv_data"]
    for x in range(count):
        collection.insert_one(rdg.get_random_customer(1, "random").dict())


def connect_db(conn, db):
    client = MongoClient(conn)
    return client[db]


def get_collection(client, col_name):
    collection = client[col_name]
    return collection


def add_customer(collection, payload):
    collection.insert_one(payload)


connection = connect_db(CONNECTION_STRING, "SCV")
collection_2 = get_collection(connection, "scv_data")
add_customer(collection_2, rdg.get_random_customer(69, "other").dict())

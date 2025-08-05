from pymongo import MongoClient
from pymongo.server_api import ServerApi


class AtlasClient:
    # can be changed later to accept username and password
    def __init__(self):
        username = "user1"
        password = "user1234"
        db = "library"
        collection = "books"

        self.__uri = uri = f"mongodb+srv://{username}:{password}@test-db.zthalkb.mongodb.net/?retryWrites=true&w=majority&appName=test-db"
        self.mongodb_client = MongoClient(self.__uri, server_api=ServerApi('1'))
        self.database = self.mongodb_client[db]
        self.collection = self.database[collection]

        # Send a ping to confirm a successful connection
        try:
            self.mongodb_client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def get_collection(self):
        return self.collection
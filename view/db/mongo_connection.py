import pymongo
import json

class ConnectDB():
    def __init__(self):
        
        with open("view/db/mongoDB.json") as Json:
            self.user_doc = json.loads(Json.read())
    
        self.mongo_url = 'mongodb+srv://'+ self.user_doc["MongoID"] + ':'+ self.user_doc['MongoPassword'] + self.user_doc["MongoURL"]
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = pymongo.database.Database(self.client, 'Cluster0')


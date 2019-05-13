import pymongo

mongo_url = 'mongodb+srv://song:yeji9140@cluster0-v0lp5.mongodb.net/test?retryWrites=true'
client = pymongo.MongoClient(mongo_url)
db = pymongo.database.Database(client,'Cluster0')
users = pymongo.collection.Collection(db,'Users')

users.insert_one({"userEmail":"0603yang@naver.com","userPassword":"1234"})




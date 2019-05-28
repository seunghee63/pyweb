import pymongo

class Book():
    def __init__(self,db):
        self.books = pymongo.collection.Collection(db,'Books')

    def BookCreate(self,bookDict):
        try:
            self.books.insert_one(bookDict)
            return True
        except:
            return False

    def getAllbooks(self):
        try:
            result = self.books.find({})
            return result
        except:
            return False

import pymongo

uri="mongodb://root:Not1f1cat1on@127.0.0.1:27001/admin"
print("test connection")
pymongo.MongoClient(uri, connect=False)

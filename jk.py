import pymongo

uri="mongodb://automationuser:everbridge@0.0.0.0:27017/ebsautomation"
print("test connection")
a=pymongo.MongoClient(uri, connect=False)
print(a.server_info())

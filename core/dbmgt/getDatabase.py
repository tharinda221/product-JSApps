# import libraries
from pymongo import MongoClient


def getDatabase():
    url = "mongodb://JSApps:JSApps@ds045465.mongolab.com:45465/jsapps"
    # url = config.database
    client = MongoClient(url)
    db = client.jsapps
    # return client.JSApps
    return db

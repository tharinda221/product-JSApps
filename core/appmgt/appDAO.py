import datetime
import logging

import math

from core.common.Constants import *
from bson.objectid import ObjectId
from core.appmgt.apps import twitterApps
from core.appmgt.apps import facebookApps
from core.appmgt.apps import facebookUserCreatable


def putFacebookAppsData():
    id = databaseCollections.facebookAppsCollectionName.insert({})
    databaseCollections.facebookAppsCollectionName.save(
        {
            "_id": ObjectId(id),
            "AppName": "Change Your profile picture to support Sri Lanka in RIO olympics 2016",
            "AppMethodName": "ProfilePicCreator",
            "AppImage": "images/appImages/facebook/" + str(id) + "/appImage.jpg",
            "AppSourceImage": "images/appImages/facebook/" + str(id) + "/background.jpg",
            "AppResultImage": "images/appImages/facebook/" + str(id) + "/appResultImage.png",
            "AppUsedCount": 0,
            "AppCreatedTime": datetime.datetime.utcnow(),
            "AppDescription": "Use this app to support Sri Lanka in RIO olympics 2016. Enjoy the App",
            "AppType": "admin",
            "AppLabel": "face",
            "AppMessage": "Change Your profile picture to support Sri Lanka in RIO olympics 2016"
        }
    )
    print id
    logging.info("Inserted FacebookApp data")


# putFacebookAppsData()

def FacebookUserCreatableAppsData(AppName, AppDescription):
    id = databaseCollections.facebookUserCreatableAppsCollectionName.insert({})
    databaseCollections.facebookUserCreatableAppsCollectionName.save(
        {
            "_id": ObjectId(id),
            "AppName": AppName,
            "AppMethodName": "ProfilePicCreator",
            "AppUsedCount": 0,
            "AppCreatedTime": datetime.datetime.utcnow(),
            "AppDescription": AppDescription,
            "AppMessage": "Change your profile picture against CEPA/ETCA",
            "AppPerentId": "56bf6355380dab5a65b7935b",
            "AppImage": "images/appImages/facebook/userApps/" + str(id) + "/appImage.jpg",
            "AppSourceImage": "images/appImages/facebook/userApps/" + str(id) + "/AppSourceImage.jpg",
            "AppFilteringImage": "images/appImages/facebook/userApps/" + str(id) + "/FilteringImage.png"
        }
    )
    logging.info("Inserted FacebookUserCreatableApp data")
    return id


def putTwitterAppsData():
    databaseCollections.twitterAppsCollectionName.insert(
        {
            "AppName": "Your Most Used Words",
            "AppMethodName": "TestMethod",
            "AppImage": "images/appImages/twitter/app1/appImage.jpg",
            "AppSourceImage": "images/appImages/twitter/app1/background.jpg",
            "AppResultImage": "images/appImages/twitter/app1/appResultImage.jpg",
            "AppUsedCount": 0,
            "AppCreatedTime": datetime.datetime.utcnow(),
            "AppDescription": "This app will read your tweets and out you mostly used words in twitter",
            "AppMessage": "This app will read your tweets and out you mostly used words in twitter"
        }
    )
    logging.info("Inserted TwitterApps data")


def rowCount(dbCollection):
    return dbCollection.count()


def NumberOfFacebookApps():
    return rowCount(databaseCollections.facebookAppsCollectionName)


def NumberOfFacebookUserCreatableApps():
    return rowCount(databaseCollections.facebookUserCreatableAppsCollectionName)


def numberOfFacebookAppPages():
    total = NumberOfFacebookApps()
    return math.ceil(total / common.numOfAppsPerPage)


def numberOfUserCreatableFacebookAppPages():
    total = NumberOfFacebookUserCreatableApps()
    return math.ceil(total / common.numOfAppsPerPage)


def getFacebookAppDetailsById(Id):
    document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(Id)})
    obj = facebookApps(appid=document["_id"],
                       appname=document["AppName"],
                       appmethodname=document["AppMethodName"],
                       appimage=document["AppImage"],
                       appresultimage=document["AppResultImage"],
                       appsourceimage=document["AppSourceImage"],
                       appusedcount=document["AppUsedCount"],
                       appdescription=document["AppDescription"],
                       apptype=document["AppType"],
                       applabel=document["AppLabel"])

    return obj


def getFacebookUserCreatableAppDetailsById(Id):
    document = databaseCollections.facebookUserCreatableAppsCollectionName.find_one({'_id': ObjectId(Id)})
    obj = facebookUserCreatable(appid=document["_id"],
                                appname=document["AppName"],
                                appmethodname=document["AppMethodName"],
                                appimage=document["AppImage"],
                                appfilteringimage=document["AppFilteringImage"],
                                appsourceimage=document["AppSourceImage"],
                                appusedcount=document["AppUsedCount"],
                                appdescription=document["AppDescription"],
                                appmessage=document["AppMessage"],
                                appparentid=document["AppPerentId"]
                                )
    return obj


def NumberOfTwitterApps():
    return rowCount(databaseCollections.twitterAppsCollectionName)


def numberOfTwitterAppPages():
    total = NumberOfTwitterApps()
    return math.ceil(total / common.numOfAppsPerPage)


def getTwitterAppDetailsById(Id):
    document = databaseCollections.twitterAppsCollectionName.find_one({'_id': ObjectId(Id)})

    obj = twitterApps(appid=document["_id"],
                      appname=document["AppName"],
                      appmethodname=document["AppMethodName"],
                      appimage=document["AppImage"],
                      appresultimage=document["AppResultImage"],
                      appsourceimage=document["AppSourceImage"],
                      appusedcount=document["AppUsedCount"],
                      appdescription=document["AppDescription"])
    return obj


def getTwitterAppsIDList():
    return databaseCollections.twitterAppsCollectionName.distinct('_id')


def getFacebookAppsIDList():
    return databaseCollections.facebookAppsCollectionName.distinct('_id')


def getFacebookUserCreatableAppsIDList(parentAppId):
    list = []
    for data in databaseCollections.facebookUserCreatableAppsCollectionName.find({"AppPerentId": parentAppId}):
        list.append(data["_id"])
    return list


def increaseAppCount(Id, count):
    try:
        databaseCollections.facebookAppsCollectionName.update_one(
            {
                '_id': ObjectId(Id)
            },
            {"$set": {
                "AppUsedCount": count
            }})
        return True
    except IOError:
        return False


def getAppIDsByLabel(label):
    list = []
    cursor = databaseCollections.facebookAppsCollectionName.find({"AppLabel": label})
    entries = cursor[:]
    for item in entries:
        obj = facebookApps(appid=item["_id"],
                           appname=item["AppName"],
                           appmethodname=item["AppMethodName"],
                           appimage=item["AppImage"],
                           appresultimage=item["AppResultImage"],
                           appsourceimage=item["AppSourceImage"],
                           appusedcount=item["AppUsedCount"],
                           appdescription=item["AppDescription"],
                           apptype=item["AppType"],
                           applabel=item["AppLabel"])
        list.append(obj)
    return list

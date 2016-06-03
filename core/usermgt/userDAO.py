import logging

from core.common.Constants import *
from core.usermgt.user import facebookUser
from core.usermgt.user import twitterUser

def putFacebookUserData(user):
    databaseCollections.userFBCollectionName.insert_one(
        {
            "userId": user.userId,
            "userName": user.userName,
            "gender": user.gender,
            "birthday": user.birthDay,
            "hometown": user.hometown,
            "email": user.email,
            "education": user.education,
            "about": user.about
        }
    )
    logging.info("Inserted facebookUser data")





def putTwitterUserData(user):
    databaseCollections.userTwitterCollectionName.insert_one(
        {
            "userId": user.userId,
            "userScreenName": user.userScreenName,
            "userName": user.userName,
            "geoLocation": user.geoLocation,
            "country": user.country,
            "userDescription": user.userDescription,
            "profileImage": user.profileImage
        }
    )
    logging.info("Inserted twitterUser data")


def putAppOwnerData(user):
    databaseCollections.appOwnerCollectionName.insert_one(
        {
            "userId": user.userId,
            "userName": user.userName,
            "gender": user.gender,
            "birthday": user.birthDay,
            "hometown": user.hometown,
            "email": user.email,
            "education": user.education,
            "about": user.about
        }
    )
    logging.info("Inserted App owners data")


def getFacebookUserAvailability(userId):
    if databaseCollections.userFBCollectionName.find({'userId': userId}).count() > 0:
        return False
    else:
        return True


def getTwitterUserAvailability(userScreenName):
    if databaseCollections.userTwitterCollectionName.find({'userScreenName': userScreenName}).count() > 0:
        return False
    else:
        return True

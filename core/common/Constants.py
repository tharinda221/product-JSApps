from config import *
from core.dbmgt.getDatabase import *


def __init__(self):
    pass


TOKENS = {}
twitterTokens = {"OAUTH_TOKEN": "", "OAUTH_TOKEN_SECRET": ""}


class common:
    def __init__(self):
        pass

    ApplicationSecret = ""
    numOfAppsPerPage = 8
    baseUrl = "http://localhost:5000"
    # baseUrl = "http://jsapps.co"


class facebookConstants:
    def __init__(self):
        pass

    graphUrl = 'https://graph.facebook.com/'
    secretKey = "ff8f450170fda495761a8eb648044904"
    appID = "1000944106647575"
    # secretKey = "ef77aabd222d3c5fe509d1984aa791f6"
    # appID = "1686276391610614"
    GraphAPIVersion = "v2.5"
    redirectURL = common.baseUrl + "/callback/facebook"
    baseGraphApiUrl = "https://graph.facebook.com/v2.5/"
    getUserInitInfoUrl = "me?fields=name,birthday,about,bio,email,education,gender," \
                         "id,hometown"
    returnURL = ""
    returnRole = ""


class twitterConstants:
    def __init__(self):
        pass

    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
    ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

    CONSUMER_KEY = "idIKJAGhBQyhMYPPvctKYz17z"
    CONSUMER_SECRET = "5q5Nb7cK8DYyYeLNuzmm4RrIa9oEIympgQJ1vJo0337JbrdXDB"

    resource_owner_key = ""
    resource_owner_secret = ""
    returnURL = ""


class databaseCollections:
    def __init__(self):
        pass

    userFBCollectionName = getDatabase().facebookUsers
    userTwitterCollectionName = getDatabase().twitterUsers
    facebookAppsCollectionName = getDatabase().facebookApps
    facebookUserCreatableAppsCollectionName = getDatabase().facebookUserCreatableApps
    twitterAppsCollectionName = getDatabase().twitterApps
    appOwnerCollectionName = getDatabase().appOwners

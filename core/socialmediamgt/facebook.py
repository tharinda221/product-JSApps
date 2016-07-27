import requests

from __init__ import *
from core.common.Constants import *
from core.usermgt.user import facebookUser
from core.usermgt.userDAO import *
from core.appmgt.appDAO import *

FACEBOOK_APP_ID = facebookConstants.appID
FACEBOOK_APP_SECRET = facebookConstants.secretKey
GRAPH_API_VERSION = facebookConstants.GraphAPIVersion
REDIRECT_URI = facebookConstants.redirectURL
returnURL = facebookConstants.returnURL

facebookUserObj = facebookUser()


def getFacebookUserInfo(accesstoken):
    url = facebookConstants.baseGraphApiUrl + facebookConstants.getUserInitInfoUrl + "&access_token=" + \
          accesstoken + ""
    resp = requests.get(url)
    response = json.loads(resp.text)
    global facebookUserObj
    facebookUserObj = facebookUser(userId=response.get("id", ""),
                                   userName=response.get("name", ""),
                                   gender=response.get("gender", ""),
                                   birthDay=response.get("birthday", ""),
                                   hometown=response.get("hometown", ""),
                                   email=response.get("email", ""),
                                   education=response.get("education", []),
                                   about=response.get("about", ""))

    if facebookConstants.returnRole == "appOwner":
        user = facebookUser(userId=facebookUserObj.userId,
                            userName=facebookUserObj.userName,
                            gender=facebookUserObj.gender,
                            birthDay=facebookUserObj.birthDay,
                            hometown=facebookUserObj.hometown,
                            email=facebookUserObj.email,
                            education=facebookUserObj.education,
                            about=facebookUserObj.about)
        putAppOwnerData(user)
    else:
        if getFacebookUserAvailability(facebookUserObj.userId):
            user = facebookUser(userId=facebookUserObj.userId,
                                userName=facebookUserObj.userName,
                                gender=facebookUserObj.gender,
                                birthDay=facebookUserObj.birthDay,
                                hometown=facebookUserObj.hometown,
                                email=facebookUserObj.email,
                                education=facebookUserObj.education,
                                about=facebookUserObj.about,
                                image="")
            putFacebookUserData(user)


# def facebookUserCreatableAppData():


def getFacebookUser():
    return facebookUserObj


def getFacebookUserJson():
    return json.dumps(facebookUserObj, default=lambda o: o.__dict__)


def getAllAlbums(accesstoken, uid):
    url = facebookConstants.baseGraphApiUrl + uid + "/albums?access_token=" + accesstoken + ""
    resp = requests.get(url)
    response = json.loads(resp.text)
    return response


def getUserProfilePic(accesstoken):
    url = facebookConstants.baseGraphApiUrl + "me/picture?width=720&height=720&access_token=" + accesstoken + ""
    # resp = requests.get(url)
    # response = json.loads(str(resp.text))
    return url


def getAlbumIdByName(accesstoken, uid, name):
    response = getAllAlbums(accesstoken, uid)
    for data in response["data"]:
        if data["name"] == name:
            return data["id"]
    return "name not found"


def getAlbumFromId(accesstoken, id):
    url = facebookConstants.baseGraphApiUrl + id + "/photos?fields=name,source,id,created_time" + "&access_token=" + \
          accesstoken + ""
    response = requests.get(url).json()
    return response


def sharePost(accesstoken, appId):
    url = facebookConstants.baseGraphApiUrl + "me/feed" + "?access_token=" + \
          accesstoken + ""
    appDetails = getFacebookAppDetailsById(appId)
    payload = {
        'message': appDetails.AppMessage,
        'link': common.baseUrl + '/facebook/appDetails/' + appId,
        'picture': common.baseUrl + url_for('static', filename='' + appDetails.AppResultImage),
        "description": appDetails.AppDescription,
        "name": session["facebookUser"]["userName"]
    }
    r = requests.post(url, data=payload)

    print(r.status_code, r.reason)


def shareGIFPost(accesstoken, appId):
    url = facebookConstants.baseGraphApiUrl + "me/feed" + "?access_token=" + \
          accesstoken + ""
    appDetails = getFacebookAppDetailsById(appId)
    payload = {
        'message': appDetails.AppMessage + "(App Link in the first comment)",
        'link': common.baseUrl + url_for('static', filename='' + appDetails.AppResultImage)
    }
    r = requests.post(url, data=payload)

    print(r.status_code, r.reason)


def shareUserCreatedPic(accesstoken, appId):
    appDetails = getFacebookUserCreatableAppDetailsById(appId)
    url = facebookConstants.baseGraphApiUrl + "me/feed" + "?access_token=" + \
          accesstoken + ""
    payload = {
        'message': appDetails.AppMessage + "(App Link in the first comment)",
        'source': common.baseUrl + "/image/" + str(appDetails.AppID)
    }
    r = requests.post(url, data=payload)
    print r

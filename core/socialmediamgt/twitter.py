from core.common.Constants import *
from core.usermgt.user import twitterUser
from core.usermgt.userDAO import *
from core.appmgt.appDAO import *
import config
# import libraries
from twython import Twython
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
from flask import session, url_for

CONSUMER_KEY = twitterConstants.CONSUMER_KEY
CONSUMER_SECRET = twitterConstants.CONSUMER_SECRET
twitterObj = twitterUser()


class NotAuthorizedException(Exception):
    pass


def getUserToken(verifier, resource_owner_key, resource_owner_secret):
    global twitterTokens
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)
    r = requests.post(url=twitterConstants.ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    return credentials.get('oauth_token')[0], credentials.get('oauth_token_secret')[0], credentials.get('screen_name')[
        0]


def getTwitterUserDetails():
    twitterAgent = Twython(twitterConstants.CONSUMER_KEY, twitterConstants.CONSUMER_SECRET,
                           session["twitter_user_token"],
                           session["twitter_user_secret"])
    resp = twitterAgent.verify_credentials(screen_name=session["screen_name"])
    global twitterObj
    twitterObj = twitterUser(resp["id_str"],
                                  session["screen_name"],
                                  resp["name"],
                                  resp.get("geo", ""),
                                  resp.get("country", ""),
                                  resp["description"],
                                  resp['profile_image_url']
                                  )
    if getTwitterUserAvailability(session["screen_name"]):
        putTwitterUserData(userId=twitterObj.userId,
                           userScreenName=twitterObj.userScreenName,
                           userName=twitterObj.userName,
                           geoLocation=twitterObj.geoLocation,
                           country=twitterObj.country,
                           userDescription=twitterObj.userDescription,
                           profileImage=twitterObj.profileImage
                           )


def getTweetsToString(userToken, userSecret):
    re = ""
    twitterAgent = Twython(twitterConstants.CONSUMER_KEY, twitterConstants.CONSUMER_SECRET,
                           userToken,
                           userSecret)
    user_timeline = twitterAgent.get_user_timeline(screen_name=session["screen_name"], count=50)
    for tweet in user_timeline:
        # print tweet['text'] + "\n"
        re = re + tweet['text'] + " "
    return re


def getTwitterUser():
    return twitterObj


def getTwitterUserJson():
    return json.dumps(twitterObj, default=lambda o: o.__dict__)


def shareTwitterPost(appId):
    appDetails = getTwitterAppDetailsById(appId)
    twitterAgent = Twython(twitterConstants.CONSUMER_KEY, twitterConstants.CONSUMER_SECRET,
                           session["twitter_user_token"],
                           session["twitter_user_secret"])
    twitterAgent.update_status_with_media(status=common.baseUrl + url_for('/facebook/appDetails/', appId=appId),
                                          media=photo(appDetails.AppResultImage))


def photo(imageLocation):
    return open(config.pathToStatic + imageLocation, 'rb')
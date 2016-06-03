# import classes
from core.common.Constants import *
from core.socialmediamgt.twitter import *
from core.uimgt.uimgt import *

# import libraries
from __init__ import *
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

REQUEST_TOKEN_URL = twitterConstants.REQUEST_TOKEN_URL
AUTHORIZE_URL = twitterConstants.AUTHORIZE_URL
ACCESS_TOKEN_URL = twitterConstants.REQUEST_TOKEN_URL

CONSUMER_KEY = twitterConstants.CONSUMER_KEY
CONSUMER_SECRET = twitterConstants.CONSUMER_SECRET
resource_owner_key = twitterConstants.resource_owner_key
resource_owner_secret = twitterConstants.resource_owner_secret

userName = ""
profileImage = ""
TwitterAppCount = NumberOfTwitterApps()
TwitterAppList = getTwitterAppsIDList()


class authorizeTwitter(Resource):
    def get(self):
        global resource_owner_key, resource_owner_secret
        twitterConstants.returnURL = request.args.get("redirect")
        oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
        r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
        credentials = parse_qs(r.content)
        resource_owner_key = credentials.get('oauth_token')[0]
        resource_owner_secret = credentials.get('oauth_token_secret')[0]

        # Authorize
        authorize_url = AUTHORIZE_URL + resource_owner_key
        return redirect(authorize_url)


class handleCallbackTwitter(Resource):
    def get(self):
        try:
            verifier = request.args.get("oauth_verifier")
            session["twitter_user_token"], session["twitter_user_secret"], session["screen_name"] = getUserToken(
                    verifier, resource_owner_key,
                    resource_owner_secret)
            getTwitterUserDetails()
            session["twitterUser"] = json.loads(getTwitterUserJson())
            return redirect(twitterConstants.returnURL[16:])

        except NotAuthorizedException:
            return 'Access was not granted or authorization failed', 403
        except:
            raise


class twitter(Resource):
    def get(self):
        global twitterTokens, noOfAppsPagesTwitter, TwitterAppCount, TwitterAppList
        startId, endId = getStartIdAndEndId(1, TwitterAppCount)
        list = getAppList(startId, endId, TwitterAppList, "twitter")
        headers = {'Content-Type': 'text/html'}
        twitterUserAuthorized = True if "twitter_user_token" in session else False
        profileImage = ""
        userName = ""
        if twitterUserAuthorized:
            profileImage = session["twitterUser"]["profileImage"]
            userName = session["twitterUser"]["userName"]
        return make_response(render_template('twitter/twitterPage.html', TwitterAuthorized=twitterUserAuthorized,
                                             profilePicture=profileImage,
                                             name=userName,
                                             noOfAppsPagesTwitter=noOfAppsPagesTwitter,
                                             twitterPageNum=1, pageTwitterAppList=list),
                             200, headers)


class getTwitterPage(Resource):
    def get(self, pageNum):
        global twitterTokens, noOfAppsPagesTwitter, twitterObj, TwitterAppCount, TwitterAppList
        startId, endId = getStartIdAndEndId(pageNum, TwitterAppCount)
        list = getAppList(startId, endId, TwitterAppList, "twitter")
        headers = {'Content-Type': 'text/html'}
        twitterUserAuthorized = True if "twitter_user_token" in session else False
        profileImage = ""
        userName = ""
        if twitterUserAuthorized:
            profileImage = session["twitterUser"]["profileImage"]
            userName = session["twitterUser"]["userName"]
        return make_response(
                render_template('twitter/twitterPage.html', TwitterAuthorized=twitterUserAuthorized,
                                profilePicture=profileImage,
                                name=userName, noOfAppsPagesTwitter=noOfAppsPagesTwitter,
                                twitterPageNum=1, pageTwitterAppList=list),
                200, headers)


class getTwitterApp(Resource):
    def get(self, appId):
        global twitterTokens, twitterObj
        twitterCommentUrl = common.baseUrl + '/twitter/' + appId
        obj = getTwitterAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        twitterUserAuthorized = True if "twitter_user_token" in session else False
        profileImage = ""
        userName = ""
        if twitterUserAuthorized:
            profileImage = session["twitterUser"]["profileImage"]
            userName = session["twitterUser"]["userName"]
        return make_response(
                render_template('twitter/twitterAppDetailPage.html', TwitterAuthorized=twitterUserAuthorized,
                                profilePicture=profileImage,
                                name=userName, appDetails=obj, twitterCommentUrl=twitterCommentUrl),
                200,
                headers)


class shareTwitterResults(Resource):
    def get(self, appId):
        shareTwitterPost(appId)
        return redirect('/twitter')

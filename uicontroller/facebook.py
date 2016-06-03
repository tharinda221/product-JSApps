__author__ = 'tharinda'
# import classes
from __init__ import *
from core.socialmediamgt.facebook import *
from core.uimgt.uimgt import *
# import libraries
from rauth import OAuth2Service
from flask_restful import Resource
from core.appmgt.appDAO import *
from core.usermgt.userDAO import *

facebookAppCount = NumberOfFacebookApps()
FacebookAppList = getFacebookAppsIDList()
facebookUserCreatableAppCount = NumberOfFacebookUserCreatableApps()
runApplicaions = facebookAppsMethods()

graph_url = 'https://graph.facebook.com/'
facebookAgent = OAuth2Service(name='facebook',
                              authorize_url='https://www.facebook.com/dialog/oauth',
                              access_token_url=graph_url + 'oauth/access_token',
                              client_id=facebookConstants.appID,
                              client_secret=facebookConstants.secretKey,
                              base_url=graph_url)


class facebookLogin(Resource):
    def get(self):
        facebookConstants.returnURL = request.args.get("redirect")
        redirect_uri = REDIRECT_URI
        params = {'redirect_uri': redirect_uri}
        return redirect(facebookAgent.get_authorize_url(**params))


class facebookAuthorized(Resource):
    def get(self):
        # make a request for the access token credentials using code
        redirect_uri = REDIRECT_URI
        data = dict(code=request.args['code'], redirect_uri=redirect_uri)
        facebookSession = facebookAgent.get_auth_session(data=data)
        session["facebook_user_token"] = facebookSession.access_token
        getFacebookUserInfo(session["facebook_user_token"])
        session["facebookUser"] = json.loads(getFacebookUserJson())
        return redirect(facebookConstants.returnURL)


class facebook(Resource):
    def get(self):
        global noOfAppsPagesFacebook, facebookUserObj, facebookAppCount, FacebookAppList
        facebookUserObj = getFacebookUser()
        startId, endId = getStartIdAndEndId(1, facebookAppCount)
        list = getAppList(startId, endId, FacebookAppList, "facebook")
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
            render_template('facebook/facebookAdminApp/facebookPage.html', authorized=userAuthorized, id=userId,
                            name=userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                            facebookPageNum=1, pageAppList=list),
            200, headers)


class getFacebookPage(Resource):
    def get(self, pageNum):
        global noOfAppsPagesFacebook, facebookUserObj, facebookAppCount, FacebookAppList
        facebookUserObj = getFacebookUser()
        startId, endId = getStartIdAndEndId(pageNum, facebookAppCount)
        list = getAppList(startId, endId, FacebookAppList, "facebook")
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
            render_template('facebook/facebookAdminApp/facebookPage.html', authorized=userAuthorized, id=userId,
                            name=userName, noOfAppsPagesFacebook=noOfAppsPagesFacebook,
                            facebookPageNum=pageNum, pageAppList=list),
            200, headers)


class getFacebookApp(Resource):
    def get(self, appId):
        global facebookUserObj
        facebookCommentUrl = common.baseUrl + '/facebook/' + appId
        facebookUserObj = getFacebookUser()
        appDetails = getFacebookAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
            return redirect('/facebook/runApplication/adminApp/' + appId)
        return make_response(
            render_template('facebook/facebookAdminApp/facebookAppDetailPage.html', authorized=userAuthorized,
                            id=userId,
                            name=userName, appDetails=appDetails, facebookCommentUrl=facebookCommentUrl),
            200, headers)


class getFacebookUserApp(Resource):
    def get(self, appId):
        global facebookUserObj
        facebookCommentUrl = common.baseUrl + '/facebook/' + appId
        facebookUserObj = getFacebookUser()
        appDetails = getFacebookUserCreatableAppDetailsById(appId)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
            render_template('facebook/userApp/appDetailsContent/appDetails.html', authorized=userAuthorized,
                            id=userId,
                            name=userName, appDetails=appDetails, facebookCommentUrl=facebookCommentUrl),
            200, headers)


class shareFacebookResults(Resource):
    def get(self, appId):
        shareUserCreatedPic(session["facebook_user_token"], appId)
        return redirect('/facebook')


class getFacebookUserCreatableApps(Resource):
    def get(self, appId, pageNum):
        global noOfUserCreatableAppsFacebook
        IdList = getFacebookUserCreatableAppsIDList(appId)
        startId, endId = getStartIdAndEndId(pageNum, facebookUserCreatableAppCount)
        appList = getUserCretableAppList(startId, endId, IdList)
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
            render_template('facebook/userApp/appContent/app.html', authorized=userAuthorized, id=userId,
                            name=userName, noOfAppsUserCreatablePagesFacebook=noOfUserCreatableAppsFacebook,
                            facebookPageNum=pageNum, pageAppList=appList),
            200, headers)

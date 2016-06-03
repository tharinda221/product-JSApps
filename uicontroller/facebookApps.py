__author__ = 'tharinda'
# import classes
from core.socialmediamgt.facebook import *
from core.appmgt.facebookApps import *
from core.appmgt.appDAO import *
from core.usermgt.userDAO import *
# import libraries
from __init__ import *

runApplicaions = facebookAppsMethods()


class runFacebookApplication(Resource):
    def get(self, appId):
        userAuthorized = True if "facebook_user_token" in session else False
        if userAuthorized:
            obj = getFacebookAppDetailsById(appId)
            # run method
            method_name = obj.AppMethodName
            method = getattr(runApplicaions, method_name)
            if not method:
                raise Exception("Method %s not implemented" % method_name)
            session["fileName"] = method(appId)
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
            facebookCommentUrl = common.baseUrl + '/facebook/' + appId
            obj = getFacebookAppDetailsById(appId)
            headers = {'Content-Type': 'text/html'}

            return make_response(
                    render_template('facebook/facebookAdminApp/facebookAppFinished.html', authorized=userAuthorized,
                                    id=userId,
                                    name=userName, appDetails=obj,
                                    facebookCommentUrl=facebookCommentUrl), 200, headers)
        else:
            return redirect('/facebook/appDetails/adminApp/' + appId)


class runFacebookUserApplication(Resource):
    def get(self, appId):
        userAuthorized = True if "facebook_user_token" in session else False
        if userAuthorized:
            obj = getFacebookUserCreatableAppDetailsById(appId)
            #run method
            method_name = obj.AppMethodName
            method = getattr(runApplicaions, method_name)
            if not method:
                raise Exception("Method %s not implemented" % method_name)
            session["fileName"] = method(appId)
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
            facebookCommentUrl = common.baseUrl + '/facebook/' + appId
            headers = {'Content-Type': 'text/html'}

            return make_response(
                    render_template('facebook/userApp/appFinished/appFinished.html', authorized=userAuthorized,
                                    id=userId,
                                    name=userName, appDetails=obj,
                                    facebookCommentUrl=facebookCommentUrl), 200, headers)
        else:
            return redirect('/facebook/appDetails/userApp/' + appId)

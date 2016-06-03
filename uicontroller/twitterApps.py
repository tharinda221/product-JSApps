__author__ = 'tharinda'
# import classes
from core.socialmediamgt.twitter import *
from core.appmgt.appDAO import *
from core.usermgt.userDAO import *
from core.appmgt.twitterApps import *
# import libraries
from __init__ import *

runTwitterApp = twitterAppsMethods()


class runTwitterApplicaions(Resource):
    def get(self, appId):
        global twitterTokens
        twitterUserAuthorized = True if "twitter_user_token" in session else False
        if twitterUserAuthorized:
            obj = getTwitterAppDetailsById(appId)
            # run method
            method_name = obj.AppMethodName
            method = getattr(runTwitterApp, method_name)
            if not method:
                raise Exception("Method %s not implemented" % method_name)
            method()
            print "Finished"
            profileImage = session["twitterUser"]["profileImage"]
            userName = session["twitterUser"]["userName"]
            twitterCommentUrl = common.baseUrl + '/twitter/' + appId
            obj = getTwitterAppDetailsById(appId)
            headers = {'Content-Type': 'text/html'}
            return make_response(
                    render_template('twitter/twitterAppFinished.html', TwitterAuthorized=twitterUserAuthorized,
                                    profilePicture=profileImage,
                                    name=userName, appDetails=obj, twitterCommentUrl=twitterCommentUrl), 200,
                    headers)
        else:
            return redirect('/twitter/appDetails/' + appId)

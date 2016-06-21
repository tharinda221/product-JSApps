from __init__ import *

from core.socialmediamgt.facebook import *
from core.appmgt.facebookApps import *
from core.appmgt.appDAO import *
from core.usermgt.userDAO import *
from core.common.Constants import *

runApplicaions = facebookAppsMethods()


class FacebookApplicationAPI(Resource):
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
            data = {
                'imageUrl': session["fileName"],
                'appId': appId,
                'facebookShare': "https://www.facebook.com/dialog/feed?app_id=1686276391610614&"
                                 "link=http://jsapps.com/facebook/appDetails/adminApp/" + str(obj.AppID) +
                                 "&picture=" +session["fileName"] + "&name=" + obj.AppName +
                                 "&caption=JSApps.co&description=" + str(obj.AppDescription)
            }
            js = json.dumps(data)
            print js
            resp = Response(js, status=200, mimetype='application/json')

            return resp
        else:
            data = {
                'error': "user not authorized"
            }
            js = json.dumps(data)

            resp = Response(js, status=200, mimetype='application/json')

            return resp

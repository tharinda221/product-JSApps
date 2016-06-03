from __init__ import *
from core.uimgt.uimgt import *
# import libraries
from core.appmgt.appDAO import *
from core.usermgt.userDAO import *

facebookAppCount = NumberOfFacebookApps()
FacebookAppList = getFacebookAppsIDList()


class createApp(Resource):
    def get(self):
        global facebookUserObj
        facebookUserObj = getFacebookUser()
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
        return make_response(
                render_template('facebook/userApp/createApp/createApp.html', authorized=userAuthorized, id=userId,
                                name=userName),
                200, headers)

    def post(self):
        global facebookUserObj
        print request.form
        id = FacebookUserCreatableAppsData(request.form['title'], request.form['description'])
        file = request.files['watermark']
        filePath = config.pathToUserImage + str(id) + "/FilteringImage.png"
        if not os.path.exists(config.pathToUserImage + str(id)):
            os.makedirs(config.pathToUserImage + str(id))
        print filePath
        file.save(filePath)
        facebookUserObj = getFacebookUser()
        headers = {'Content-Type': 'text/html'}
        userAuthorized = True if "facebook_user_token" in session else False
        userId = ""
        userName = ""
        if userAuthorized:
            userId = session["facebookUser"]["userId"]
            userName = session["facebookUser"]["userName"]
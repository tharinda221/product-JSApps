__author__ = 'tharinda'

# import classes
from uicontroller.facebook import *
from uicontroller.index import *
from uicontroller.facebookApps import *
from uicontroller.twitterApps import *
from uicontroller.twitter import *
from uicontroller.about import *
from uicontroller.privacy import *
from uicontroller.createApp import *
from uicontroller.ApplicationAPI import *
# import libraries
import flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_object(__name__)
api = Api(app)

api.add_resource(main, '/', endpoint='/')
api.add_resource(facebook, '/facebook', endpoint='/facebook')
api.add_resource(twitter, '/twitter', endpoint='/twitter')
api.add_resource(facebookLogin, '/authorize/facebook', endpoint='/authorize/facebook')
api.add_resource(facebookAuthorized, '/callback/facebook')
api.add_resource(authorizeTwitter, '/authorize/twitter', endpoint='/authorize/twitter')
api.add_resource(handleCallbackTwitter, '/callback/twitter', endpoint='/callback/twitter')
api.add_resource(getFacebookPage, '/facebook/<int:pageNum>', endpoint='/facebook/')
api.add_resource(getFacebookApp, '/facebook/appDetails/adminApp/<appId>',
                 endpoint='/facebook/appDetails/adminApp/appId')
api.add_resource(getFacebookUserApp, '/facebook/appDetails/userApp/<appId>',
                 endpoint='/facebook/appDetails/userApp/appId')
api.add_resource(getFacebookUserCreatableApps, '/facebook/UserCreatableAppsDetails/<appId>/<int:pageNum>')
api.add_resource(runFacebookApplication, '/facebook/runApplication/adminApp/<appId>',
                 endpoint='/facebook/runApplication/adminApp/<appId>')
api.add_resource(runFacebookUserApplication, '/facebook/runApplication/userApp/<appId>',
                 endpoint='/facebook/runApplication/userApp/<appId>')
api.add_resource(getTwitterPage, '/twitter/<int:pageNum>', endpoint='/twitter/')
api.add_resource(getTwitterApp, '/twitter/appDetails/<appId>', endpoint='/twitter/appDetails/')
api.add_resource(runTwitterApplicaions, '/twitter/runApplication/<appId>', endpoint='/twitter/runApplication/')
api.add_resource(shareFacebookResults, '/facebook/share/<appId>', endpoint='/facebook/share')
api.add_resource(shareTwitterResults, '/twitter/share/<appId>', endpoint='/twitter/share')
api.add_resource(about, '/about', endpoint='/about')
api.add_resource(privacy, '/privacy', endpoint='/privacy')

api.add_resource(createApp, '/facebook/createApp', endpoint='/facebook/createApp')
# api.add_resource(ImageRendering, '/image/<appName>')
api.add_resource(FacebookApplicationAPI, '/facebook/getResultImage/<appId>')
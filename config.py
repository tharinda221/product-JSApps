__author__ = 'tharinda'

# import libraries
import os
from flask import json
from controller import *

app.secret_key = os.urandom(24)
app.debug = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AppsImagePath = BASE_DIR + "/product-JSApps/static/images/appImages/"
facebookUserAppsImagePath = BASE_DIR + "/product-JSApps/static/images/appImages/facebook/userApps/"
fontPath = BASE_DIR + "/product-JSApps/static/fonts/"
pathToStatic = BASE_DIR + "/product-JSApps/static/"
serverImagePath = "/home/ubuntu/product-JSApps/static/images/appImages/facebook/"
pathToUserImage = BASE_DIR + "/product-JSApps/static/images/appImages/facebook/userApps/"
pathToAppsImage = BASE_DIR + "/product-JSApps/static/images/appImages/facebook/"

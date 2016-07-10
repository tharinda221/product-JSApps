import logging

from __init__ import *
# import libraries
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import config


class main(Resource):
    def get(self):
        return redirect('/facebook')


class ImageRendering(Resource):
    def get(self, appName):
        pilImage = open(config.pathToAppsImage + appName + '/result/' +
                        str(session["facebookUser"]["userId"]) + ".jpg", 'rb')
        # response = send_file(tempFileObj, as_attachment=True, attachment_filename='image.jpg')
        response = send_file(pilImage, mimetype='image/jpeg')
        return response

import logging
import re

from io import BytesIO
import StringIO
from __init__ import *
# import libraries
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
import config
from ApplicationAPI import *
from base64 import decodestring
class main(Resource):
    def get(self):
        return redirect('/facebook')


class ImageRendering(Resource):
    def get(self, appName):
        img_str = getFacebookUserImage(session["facebookUser"]["userId"])
        OutputImage = cStringIO.StringIO()
        image_string = cStringIO.StringIO(base64.b64decode(img_str))
        image = Image.open(image_string)
        image.save(OutputImage, image.format, quality=100)
        OutputImage.seek(0)
        # OutputImage.save("test.jpg")
        # OutputImage = Image.open(BytesIO(base64.b64decode(img_str)))
        if OutputImage == "opencv":
            pilImage = open(config.pathToAppsImage + appName + '/result/' +
                            str(session["facebookUser"]["userId"]) + ".jpg", 'rb')
            # response = send_file(tempFileObj, as_attachment=True, attachment_filename='image.jpg')
            response = send_file(pilImage, mimetype='image/jpeg')
            return response
        else:
            response = send_file(OutputImage, mimetype='image/jpeg')
            return response

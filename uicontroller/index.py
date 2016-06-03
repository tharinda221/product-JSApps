import logging

from __init__ import *
# import libraries
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove


class main(Resource):
    def get(self):
        return redirect('/facebook')


class tempImage(Resource):
    def get(self, appId):
        logging.error("user Request image")
        tempFileObj = NamedTemporaryFile(mode='w+b', suffix='jpg')
        # pilImage = open('/home/tharinda/Working/projects/JSApps/static/images/appImages/facebook/app1/appImage.jpg',
        #                 'rb')
        pilImage = open(session["fileName"], 'rb')
        copyfileobj(pilImage, tempFileObj)
        pilImage.close()
        remove(session["fileName"])
        tempFileObj.seek(0, 0)
        response = send_file(tempFileObj, as_attachment=True, attachment_filename='image.jpg')
        return response

# import classes
import config
from core.socialmediamgt.twitter import *
from flask import session
# import libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class twitterAppsMethods(object):
    def TestMethod(self):
        text = getTweetsToString(session["twitter_user_token"], session["twitter_user_secret"])
        splitStr = text.split(' ')
        count = 0
        map = {}

        while count < splitStr.__len__():
            if splitStr[count] in map:
                map[splitStr[count]] = map[splitStr[count]] + 1
                count = count + 1
            else:
                map[splitStr[count]] = 1
                count = count + 1

        sortedMap = sorted(map, key=map.__getitem__, reverse=True)

        size = 1024, 1024
        imagepath = config.AppsImagePath
        img = Image.open(imagepath + 'twitter/app1/background.jpg')
        img.thumbnail(size, Image.ANTIALIAS)

        if 5 < len(sortedMap):
            numOfImages = 5
        else:
            numOfImages = len(sortedMap)

        insertImages = 0

        while insertImages < numOfImages:
            draw = ImageDraw.Draw(img)
            fontPath = config.fontPath
            font = ImageFont.truetype(fontPath + "Aaargh.ttf", 16 * (5 - insertImages))
            draw.text((insertImages * 100, insertImages * 100), sortedMap[insertImages], (0, 0, 0), font=font)
            insertImages = insertImages + 1

        img.save(imagepath + 'twitter/app1/appResultImage.jpg')

        img.show()

# import libraries
import logging
import urllib
from PIL import Image, ImageSequence
from PIL import ImageFont
from PIL import ImageDraw

import requests
import numpy as np
from StringIO import StringIO
from core.imageProcessing.libs.imagesTogif import writeGif
# import classes
import config


def writeTextToImage(text):
    BASE_DIR = config.BASE_DIR
    inputFilePath = BASE_DIR + "/JSApps/static/images/appImages/input.jpg"
    outputFilePath = BASE_DIR + "/JSApps/static/images/appImages/output.jpg"
    fontPath = BASE_DIR + "/JSApps/static/fonts/sans-serif.ttf"
    img = Image.open(inputFilePath)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(fontPath, 24)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((0, 0), text, (0, 0, 0), font=font)
    img.save(outputFilePath)


def readImageFromURL(url, x, y):
    response = requests.get(url, verify=False)
    # img = np.array(Image.open(StringIO(response.content)))
    file = StringIO(response.content)
    img = Image.open(file)
    image = img.resize((x, y), Image.ANTIALIAS)
    return image


def createGIF(images, filename):
    writeGif(filename, images, duration=0.5)


def findSoulMate(gender, skill):
    celebrity, celebURL = "", ""
    if gender == "male":
        if skill == 0:
            celebrity = "sunny leone"
            celebURL = "http://media2.intoday.in/indiatoday/images/stories/sunny-leone-story_650_051615105431.jpg"
        elif skill == 1:
            celebrity = "Lisa Ann"
            celebURL = "http://cdn.slamonline.com/wp-content/uploads/2016/03/lisaann_fv.jpg"
        elif skill == 2:
            celebrity = "deepika padukone"
            celebURL = "http://i1.tribune.com.pk/wp-content/uploads/2015/11/983087-deepika-1446369022-581-640x480.jpg"
        elif skill == 3:
            celebrity = "Sonakshi Sinha"
            celebURL = "http://i1.tribune.com.pk/wp-content/uploads/2015/08/932042-sinha-1438675561-507-640x480.jpg"
        elif skill == 4:
            celebrity = "Tharu Kumara"
            celebURL = "https://i.ytimg.com/vi/1CYflZReeEE/hqdefault.jpg"
        elif skill == 5:
            celebrity = "Ishitha balha"
            celebURL = "http://ytimg.googleusercontent.com/vi/NRzEmEier8s/0.jpg"
        else:
            celebrity = "emma watson"
            celebURL = "http://s3-us-west-2.amazonaws.com/ruuvy-snooki-uploads/wp-content/uploads/2016/03/02/02093445/Nicole-Snooki-Polizzi-Emma-Watson-Sex-Website-Subscriber-Feminism.jpg"
    else:
        if skill == 0:
            celebrity = "Raman Balha"
            celebURL = "http://3.bp.blogspot.com/-7SHgAg05PQI/VT3cCrKG4UI/AAAAAAAADVo/lDJ_dURj_gw/s1600/raman.jpg"
        elif skill == 1:
            celebrity = "Tharu Kumara"
            celebURL = "https://i.ytimg.com/vi/1CYflZReeEE/hqdefault.jpg"
        elif skill == 2:
            celebrity = "ranbir kapoor"
            celebURL = "http://economictimes.indiatimes.com/photo/48239734.cms"
        elif skill == 3:
            celebrity = "justin bieber"
            celebURL = "http://pixel.nymag.com/imgs/daily/vulture/2016/01/04/4-justin-bieber-cornrows.w529.h529.jpg"
        elif skill == 4:
            celebrity = "Daniel Radcliffe"
            celebURL = "http://instinctmagazine.com/sites/instinctmagazine.com/files/images/blog_posts/Nigel%20Campbell/2016/01/24/daniel%20radcliffe.jpg"
        elif skill == 5:
            celebrity = "Bill Gates"
            celebURL = "http://aib.edu.au/blog/wp-content/uploads/2015/08/bill-gates-jpg.jpg"
        else:
            celebrity = "shahrukh khan"
            celebURL = "https://hilleletv.files.wordpress.com/2015/11/shahrukhkhan-jan30.jpg"

    return celebrity, celebURL

def findFirstVehicle(number):
    name, url = "", ""
    if number == 0:
        name = "An Old, Turquoise Chevy Pick-up"
        url = "http://cars.trsty.com/wp-content/uploads/2015/06/an-old-turquoise-chevy-pick-up.jpg"
    elif number == 1:
        name = "Range Rover"
        url = "http://www.landroverftmyers.com/wp-content/uploads/2015/10/Evoque.jpg"
    elif number == 2:
        name = "honda-navi-off-road"
        url = "http://forum.maxabout.com/uploads/default/original/2X/3/36271901354c70508431b035a1443b7b18bff650.jpg"
    elif number == 3:
        name = "2016 Honda FCV and new hybrids"
        url = "http://icdn6.digitaltrends.com/image/honda-fcv-concept-das2015t_03-970x647-c.jpg"
    elif number == 4:
        name = "Trishaw"
        url = "https://travel2penang.files.wordpress.com/2012/08/trishaw02.jpg"
    else :
        name = "Three Wheel"
        url = "http://images.adspot.lk/wp-content/uploads/2015/11/04205208/large-green-440x340.png"

    return name, url

def writeTextInImage(text, img, fontSize, x, y):
    draw = ImageDraw.Draw(img)
    logging.error(config.fontPath + "sans-serif.ttf")
    font = ImageFont.truetype(config.fontPath + "sans-serif.ttf", fontSize)
    draw.text((x, y), text, (0, 0, 0), font=font)
    return img

# import libraries

import dateutil.parser as parser
from random import randint
import time

# import classes
from core.socialmediamgt.facebook import *
from core.imageProcessing.Operations import *
from core.usermgt.user import *
from core.common.Constants import *
import config
from core.imageProcessing.libs.cartoonify import *
from core.imageProcessing.libs.pencil import *

delay = 0


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


def fileRemove(dirPath, filePath):
    if os.path.isdir(dirPath):
        if os.path.exists(filePath):
            os.remove(filePath)
    else:
        os.makedirs(dirPath)


class facebookAppsMethods(object):
    def togetherAllProfilePicsByYear(self):
        profileSourceArray = []
        profilePicsArray = getAlbumFromId(TOKENS["user_token"],
                                          getAlbumIdByName(TOKENS["user_token"], User.userId, "Profile Pictures"))[
            "data"]
        for data in profilePicsArray:
            if parser.parse(data["created_time"]).year == 2015:
                profileSourceArray.append(data["source"])
        print(profileSourceArray)

    def PredictByBirthNumber(self):
        BASE_DIR = config.BASE_DIR
        DataPath = open(os.path.join(BASE_DIR, "JSApps/resources/", "appData.json"), "r")
        data = json.load(DataPath)["App1"]["data"][0]["prediction"]
        writeTextToImage(data)

    def TestMethod(self, appId):
        print("Method Accessed")
        document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        background = Image.open(config.pathToStatic + document["AppResultImage"])
        fileName = str(random_with_N_digits(24))
        print config.AppsImagePath + "facebook/app1/" + fileName + ".jpg"
        background.save(config.AppsImagePath + "facebook/app1/" + fileName + ".jpg")
        return config.AppsImagePath + "facebook/app1/" + fileName + ".jpg"

    def profileImagesOnAGif(self, appId):
        profilePicsAlbumId = getAlbumIdByName(session["facebook_user_token"], session["facebookUser"]["userId"],
                                              "Profile Pictures")
        profilePicslist = getAlbumFromId(session["facebook_user_token"], profilePicsAlbumId)['data']
        profilePicsURLlist = []
        for profPics in profilePicslist:
            profilePicsURLlist.append(profPics['source'])
        images = []
        for profPicURL in profilePicsURLlist:
            images.append(readImageFromURL(profPicURL))
        fileName = str(random_with_N_digits(24))
        directory = config.pathToAppsImage + appId
        if not os.path.exists(directory):
            os.makedirs(directory)
        createGIF(images=images, filename=directory + "/" + fileName + ".gif")
        return directory + "/" + fileName + ".gif"

    def ProfilePicCreator(self, appId):
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + str(appId) + "/result"
        filePath = config.pathToAppsImage + str(appId) + "/result" + "/" + fileName + ".jpg"
        fileRemove(dirPath, filePath)
        document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        url = getUserProfilePic(session["facebook_user_token"])
        background = readImageFromURL(url, 500, 500)
        foreground = Image.open(config.pathToStatic + document["AppSourceImage"])
        background.paste(foreground, (0, 0), foreground)
        # save
        background.save(filePath)
        return common.baseUrl + "/static/images/appImages/facebook/" + str(appId) + "/result" + "/" + fileName + ".jpg"

    def CelebrityDatingMatch(self, appId):
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app1" + "/result"
        filePath = config.pathToAppsImage + "app1" + "/result" + "/" + fileName + ".jpg"
        fileRemove(dirPath, filePath)
        document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        url = getUserProfilePic(session["facebook_user_token"])
        skill = randint(0, 6)
        celeb, celebUrl = findSoulMate(session["facebookUser"]["gender"], skill)
        userImage = readImageFromURL(url, 245, 245)
        celebImage = readImageFromURL(celebUrl, 245, 245)
        background = Image.open(config.pathToStatic + document["AppSourceImage"])
        background.paste(userImage, (70, 170))
        background.paste(celebImage, (488, 170))
        writeTextInImage(session["facebookUser"]["userName"], background, 30, 70, 450, "black")
        writeTextInImage(celeb, background, 30, 488, 450, "black")
        background.save(filePath)
        # time.sleep(delay)
        return common.baseUrl + "/static/images/appImages/facebook/app1/" + "result" + "/" + fileName + ".jpg"
        # return common.baseUrl + "/image/app1", background

    def vehicleFind(self, appId):
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app2" + "/result"
        filePath = config.pathToAppsImage + "app2" + "/result" + "/" + fileName + ".jpg"
        fileRemove(dirPath, filePath)
        document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        profileUrl = getUserProfilePic(session["facebook_user_token"])
        number = randint(0, 5)
        name, Url = findFirstVehicle(number)
        userImage = readImageFromURL(profileUrl, 245, 245)
        vehicleImage = readImageFromURL(Url, 400, 300)
        background = Image.open(config.pathToStatic + document["AppSourceImage"])
        background.paste(userImage, (51, 181))
        background.paste(vehicleImage, (320, 150))
        writeTextInImage(session["facebookUser"]["userName"], background, 25, 37, 450, "white")
        writeTextInImage(name, background, 25, 330, 450, "white")
        # return config.pathToAppsImage + "app1" + "/" + fileName + ".jpg"
        background.save(filePath)
        # time.sleep(delay)
        return common.baseUrl + "/static/images/appImages/facebook/app2/" + "result" + "/" + fileName + ".jpg"
        # return common.baseUrl + "/image/app2", background

    def cartooning(self, appId):
        # document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        # save file
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app3" + "/result"
        filePath = config.pathToAppsImage + "app3" + "/result" + "/" + fileName + ".jpg"
        fileRemove(dirPath, filePath)
        url = getUserProfilePic(session["facebook_user_token"])
        userImage = readImageFromURLCV2(url, 500, 500)
        tmp_canvas = Cartoonizer()
        output = tmp_canvas.render(userImage)
        cv2_im = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(cv2_im)
        foreground = Image.open(config.pathToCommon + "jsapps.png")
        background.paste(foreground, (0, 0), foreground)
        # time.sleep(delay)
        background.save(filePath)
        return common.baseUrl + "/static/images/appImages/facebook/app3/" + "result" + "/" + fileName + ".jpg"
        # return common.baseUrl + "/image/app3", "opencv"

    def pencilSketch(self, appId):
        # document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app4" + "/result"
        filePath = config.pathToAppsImage + "app4" + "/result" + "/" + fileName + ".jpg"
        fileRemove(dirPath, filePath)
        url = getUserProfilePic(session["facebook_user_token"])
        userImage = readImageFromURLCV2(url, 500, 500)
        pencil = PencilSketch((500, 500))
        output = pencil.render(userImage)
        cv2_im = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        background = Image.fromarray(cv2_im)
        foreground = Image.open(config.pathToCommon + "jsapps.png")
        background.paste(foreground, (0, 0), foreground)
        # save file
        background.save(filePath)
        # time.sleep(delay)
        return common.baseUrl + "/static/images/appImages/facebook/app4/" + "result" + "/" + fileName + ".jpg"

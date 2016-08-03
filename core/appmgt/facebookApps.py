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

delay = 1


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


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
        document = databaseCollections.facebookUserCreatableAppsCollectionName.find_one({'_id': ObjectId(appId)})
        url = getUserProfilePic(session["facebook_user_token"])
        background = readImageFromURL(url)
        foreground = Image.open(config.pathToStatic + document["AppFilteringImage"])
        background.paste(foreground, (0, 0), foreground)
        fileName = str(random_with_N_digits(24))
        background.save(config.pathToUserImage + appId + "/" + fileName + ".jpg")
        return config.pathToUserImage + appId + "/" + fileName + ".jpg"

    def CelebrityDatingMatch(self, appId):
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
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app1" + "/result"
        filePath = config.pathToAppsImage + "app1" + "/result" + "/" + fileName + ".jpg"
        if os.path.isdir(dirPath):
            if os.path.exists(filePath):
                os.remove(filePath)
                background.save(filePath)
            else:
                background.save(filePath)
        else:
            os.makedirs(dirPath)
            background.save(filePath)
        time.sleep(delay)
        return common.baseUrl + "/static/images/appImages/facebook/app1/" + "result" + "/" + fileName + ".jpg"
        # return common.baseUrl + "/image/app1", background

    def vehicleFind(self, appId):
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
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app2" + "/result"
        filePath = config.pathToAppsImage + "app2" + "/result" + "/" + fileName + ".jpg"
        if os.path.isdir(dirPath):
            if os.path.exists(filePath):
                os.remove(filePath)
                background.save(filePath)
            else:
                background.save(filePath)
        else:
            os.makedirs(dirPath)
            background.save(filePath)
        # return config.pathToAppsImage + "app1" + "/" + fileName + ".jpg"
        time.sleep(delay)
        return common.baseUrl + "/static/images/appImages/facebook/app2/" + "result" + "/" + fileName + ".jpg"
        # return common.baseUrl + "/image/app2", background

    def cartooning(self, appId):
        # document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        url = getUserProfilePic(session["facebook_user_token"])
        userImage = readImageFromURLCV2(url, 500, 500)
        tmp_canvas = Cartoonizer()
        output = tmp_canvas.render(userImage)
        # save file
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app3" + "/result"
        filePath = config.pathToAppsImage + "app3" + "/result" + "/" + fileName + ".jpg"
        if os.path.isdir(dirPath):
            if os.path.exists(filePath):
                os.remove(filePath)
                # output.save(filePath)
                cv2.imwrite(filePath, output)
            else:
                # output.save(filePath)
                cv2.imwrite(filePath, output)
        else:
            os.makedirs(dirPath)
            # output.save(filePath)
            cv2.imwrite(filePath, output)
        time.sleep(delay)
        return common.baseUrl + "/static/images/appImages/facebook/app3/" + "result" + "/" + fileName + ".jpg"
        # return common.baseUrl + "/image/app3", "opencv"

    def pencilSketch(self, appId):
        # document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        url = getUserProfilePic(session["facebook_user_token"])
        userImage = readImageFromURLCV2(url, 500, 500)
        pencil = PencilSketch((500, 500))
        output = pencil.render(userImage)
        cv2.rectangle(output, (450, 0), (500, 20), (255, 0, 0), -1)
        cv2.putText(output, "JSApps.co", (460, 10), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        # save file
        fileName = str(session["facebookUser"]["userId"])
        dirPath = config.pathToAppsImage + "app4" + "/result"
        filePath = config.pathToAppsImage + "app4" + "/result" + "/" + fileName + ".jpg"
        if os.path.isdir(dirPath):
            if os.path.exists(filePath):
                os.remove(filePath)
                # output.save(filePath)
                cv2.imwrite(filePath, output)
            else:
                # output.save(filePath)
                cv2.imwrite(filePath, output)
        else:
            os.makedirs(dirPath)
            # output.save(filePath)
            cv2.imwrite(filePath, output)
        time.sleep(delay)
        return common.baseUrl + "/static/images/appImages/facebook/app4/" + "result" + "/" + fileName + ".jpg"

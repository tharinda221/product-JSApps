# import libraries

import dateutil.parser as parser
from random import randint
# import classes
from core.socialmediamgt.facebook import *
from core.imageProcessing.Operations import *
from core.usermgt.user import *
from core.common.Constants import *
import config
from core.imageProcessing.libs.cartoonify import *

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
        userImage = readImageFromURL(url, 150, 150)
        celebImage = readImageFromURL(celebUrl, 150, 150)
        background = Image.open(config.pathToStatic + document["AppSourceImage"])
        background.paste(userImage, (37, 127))
        background.paste(celebImage, (436, 127))
        writeTextInImage(session["facebookUser"]["userName"], background, 20, 37, 290)
        writeTextInImage(celeb, background, 20, 436, 290)
        fileName = str(session["facebookUser"]["userId"])
        dirPath= config.pathToAppsImage + "app1" + "/result"
        filePath= config.pathToAppsImage + "app1" + "/result" + "/" + fileName + ".jpg"
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
        return common.baseUrl + "/static/images/appImages/facebook/app1/" + "result" + "/" + fileName + ".jpg"

    # def cartooning(self, appId):
    #     document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
    #     url = getUserProfilePic(session["facebook_user_token"])
    #     userImage = readImageFromURL(url, 500, 500)
    #     output = cartoonize(userImage)
    #     output = Image.fromarray(output)
    #     # save file
    #     fileName = str(session["facebookUser"]["userId"])
    #     dirPath = config.pathToAppsImage + "app2" + "/result"
    #     filePath = config.pathToAppsImage + "app2" + "/result" + "/" + fileName + ".jpg"
    #     if os.path.isdir(dirPath):
    #         if os.path.exists(filePath):
    #             os.remove(filePath)
    #             output.save(filePath)
    #         else:
    #             output.save(filePath)
    #     else:
    #         os.makedirs(dirPath)
    #         output.save(filePath)
    #     return common.baseUrl + "/static/images/appImages/facebook/app2/" + "result" + "/" + fileName + ".jpg"

    def vehicleFind(self, appId):
        document = databaseCollections.facebookAppsCollectionName.find_one({'_id': ObjectId(appId)})
        profileUrl = getUserProfilePic(session["facebook_user_token"])
        skill = randint(0, 6)
        celeb, celebUrl = findSoulMate(session["facebookUser"]["gender"], skill)

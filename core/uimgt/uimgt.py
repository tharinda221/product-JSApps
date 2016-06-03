# import classes

from core.common.Constants import *
from core.appmgt.facebookApps import *

noOfAppsPagesFacebook = numberOfFacebookAppPages() + 1
noOfAppsPagesTwitter = numberOfTwitterAppPages() + 1
noOfUserCreatableAppsFacebook = numberOfUserCreatableFacebookAppPages() +1

def getAppList(startId, endId, appList, socialname):
    list = []
    count = endId
    for i in range(endId, startId + 1):
        if socialname == "facebook":
            list.append(getFacebookAppDetailsById(appList[count]))
        elif socialname == "twitter":
            list.append(getTwitterAppDetailsById(appList[count]))
        count += 1
    return list


def getUserCretableAppList(startId, endId, appList):
    list = []
    count = endId
    for i in range(endId, startId + 1):
        list.append(getFacebookUserCreatableAppDetailsById(appList[count]))
        count += 1
    return list


def getStartIdAndEndId(PageNum, appCount):
    startId = (appCount - 1) - ((PageNum - 1) * common.numOfAppsPerPage)
    if (startId - (common.numOfAppsPerPage - 1)) > 0:
        endId = startId - (common.numOfAppsPerPage - 1)
        return startId, endId
    else:
        endId = 0
        return startId, endId

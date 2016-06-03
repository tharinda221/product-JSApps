class facebookApps(object):
    def __init__(self, appid="",
                 appname="",
                 appmethodname="",
                 appimage="",
                 appsourceimage="",
                 appresultimage="",
                 appusedcount="",
                 appcreatedtimedate="",
                 appdescription="",
                 appmessage="",
                 apptype=""
                 ):
        self.AppType = apptype
        self.AppMessage = appmessage
        self.AppDescription = appdescription
        self.AppCreatedTimeDate = appcreatedtimedate
        self.AppUsedCount = appusedcount
        self.AppResultImage = appresultimage
        self.AppSourceImage = appsourceimage
        self.AppImage = appimage
        self.AppMethodName = appmethodname
        self.AppName = appname
        self.AppID = appid


class facebookUserCreatable(object):
    def __init__(self, appid="",
                 appname="",
                 appmethodname="",
                 appimage="",
                 appsourceimage="",
                 appfilteringimage="",
                 appusedcount="",
                 appcreatedtimedate="",
                 appdescription="",
                 appmessage="",
                 appparentid=""
                 ):
        self.AppParentId = appparentid
        self.AppMessage = appmessage
        self.AppDescription = appdescription
        self.AppCreatedTimeDate = appcreatedtimedate
        self.AppUsedCount = appusedcount
        self.AppFilteringImage = appfilteringimage
        self.AppSourceImage = appsourceimage
        self.AppImage = appimage
        self.AppMethodName = appmethodname
        self.AppName = appname
        self.AppID = appid


class twitterApps(object):
    def __init__(self, appid="",
                 appname="",
                 appmethodname="",
                 appimage="",
                 appsourceimage="",
                 appresultimage="",
                 appusedcount="",
                 appcreatedtimedate="",
                 appdescription="",
                 appmessage=""
                 ):
        self.AppMessage = appmessage
        self.AppDescription = appdescription
        self.AppCreatedTimeDate = appcreatedtimedate
        self.AppUsedCount = appusedcount
        self.AppResultImage = appresultimage
        self.AppSourceImage = appsourceimage
        self.AppImage = appimage
        self.AppMethodName = appmethodname
        self.AppName = appname
        self.AppID = appid

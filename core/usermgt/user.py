class facebookUser:
    def __init__(self, userId="",
                 userName="",
                 gender="",
                 birthDay="",
                 hometown="",
                 email="",
                 education=[],
                 about=""
                 ):
        self.about = about
        self.education = education
        self.email = email
        self.hometown = hometown
        self.birthDay = birthDay
        self.gender = gender
        self.userName = userName
        self.userId = userId


class twitterUser(object):
    def __init__(self, userId="",
                 userScreenName="",
                 userName="",
                 geoLocation="",
                 country="",
                 userDescription="",
                 profileImage=""
                 ):
        self.userDescription = userDescription
        self.profileImage = profileImage
        self.geoLocation = geoLocation
        self.country = country
        self.userName = userName
        self.userScreenName = userScreenName
        self.userId = userId

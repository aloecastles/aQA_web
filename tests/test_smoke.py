import time
from model.groupFTTBlogin import GroupLogin
from model.groupPersonalData import GroupPD

def test_applicationLaunch(app):
    app.applicationLaunch()
def test_searchOpen(app):
    app.searchOpen()
    app.searchQuery(Query="суперсила")
    app.firstSearchResultOpen()
    app.VODplayer.CenterButtonPlayClick()
    app.session.loginPageFromVOD_PA_Click()
    app.session.loginPageFromVodPA_emailFieldType(GroupLogin(FTTBlogin="demo_autotest"))
    app.session.loginPagePA_passwordType(GroupLogin(FTTBpassword="123456"))
    app.session.loginPagePA_loginBittonClick()
    app.VODplayer.VolumeOff()
    app.VODplayer.PauseClick()
    app.session.profileOpen()
    app.profile.firstNameChangeAdd(GroupPD(FirstName="3"))
    app.profile.EmailChangeAdd(GroupPD(Email="1"))
    app.profile.LastNameChangeAdd(GroupPD(LastName="2"))
    time.sleep(4)
    # app.profile.buttonSaveClick()
    time.sleep(1)
    app.session.profileLogout()


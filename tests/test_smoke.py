import time
from model.groupFTTBlogin import GroupLogin
from model.groupPersonalData import GroupPD

def test_loginAndRename(app):
    app.applicationLaunch()
    app.searchOpen()
    app.searchQuery(Query="суперсила")
    app.firstSearchResultOpen()
    app.VODplayer.CenterButtonPlayClick()
    app.session.loginPagePA_Click()
    app.session.loginPagePA_emailFieldType(GroupLogin(FTTBlogin="demo_autotest"))
    app.session.loginPagePA_passwordType(FTTBpassword="123456")
    app.session.loginPagePA_loginBittonClick()
    app.VODplayer.VolumeOff()
    app.VODplayer.PauseClick()
    app.session.profileOpen()
    app.profile.firstNameChangeAdd(GroupPD(FirstName="3"))
    app.profile.buttonSaveClick()
    time.sleep(1)
    app.session.profileLogout()


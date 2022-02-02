import time
from model.groupFTTBlogin import Group

def test_loginAndRenameRevert(app):
    app.applicationLaunch()
    app.searchOpen()
    app.searchQuery(Query="суперсила")
    app.firstSearchResultOpen()
    app.VODplayer.CenterButtonPlayClick()
    app.session.loginPagePA_Click()
    app.session.loginPagePA_emailFieldType(Group(FTTBlogin="demo_autotest"))
    app.session.loginPagePA_passwordType(FTTBpassword="123456")
    app.session.loginPagePA_loginBittonClick()
    app.VODplayer.VolumeOff()
    app.VODplayer.PauseClick()
    app.session.profileOpen()
    app.profile.firstNameClear()
    app.profile.firstNameChangeAdd(firstName="demo_autotest")
    app.profile.buttonSaveClick()
    time.sleep(5)
    app.session.profileLogout()

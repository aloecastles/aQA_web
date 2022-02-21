import time
from model.groupFTTBlogin import GroupLogin
from model.groupPersonalData import GroupPD

def test_applicationLaunch(app):
    app.applicationLaunch()
def test_sessionProfileOpen(app):
    app.session.signInOpen()
def test_loginPageFromHome_PA_Click(app):
    app.session.loginPageFromHome_PA_Click()
def test_4(app):
    app.session.loginPageFromHomePA_emailFieldType(GroupLogin(FTTBlogin="demo_autotest"))
def test_5(app):
    app.session.loginPagePA_passwordType(GroupLogin(FTTBpassword="123456"))
def test_6(app):
    app.session.loginPagePAfromHome_loginButtonClick()
def test_7(app):
    app.searchOpen()
def test_8(app):
    app.searchQuery(Query="суперсила")
def test_9(app):
    app.firstSearchResultOpen()
def test_10(app):
    app.VODplayer.CenterButtonPlayClick()
    app.session.profileOpen()
    # app.session.profileLogoutClick()
    time.sleep(2)
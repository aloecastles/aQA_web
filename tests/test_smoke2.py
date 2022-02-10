import time
from model.groupFTTBlogin import GroupLogin
from model.groupPersonalData import GroupPD

def test_applicationLaunch(app):
    app.applicationLaunch()
def test_sessionProfileOpen(app):
    app.session.signInOpen()
def test_loginPageFromHome_PA_Click(app):
    app.session.loginPageFromHome_PA_Click()
    app.session.loginPageFromHomePA_emailFieldType(GroupLogin(FTTBlogin="demo_autotest"))
    app.session.loginPagePA_passwordType(GroupLogin(FTTBpassword="123456"))
    app.session.loginPagePAfromHome_loginButtonClick()
    app.session.profileOpen()
    # app.session.profileLogoutClick()
    time.sleep(2)
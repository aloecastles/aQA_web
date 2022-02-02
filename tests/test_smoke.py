import time
import pytest
from model.groupFTTBlogin import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
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
    app.profile.firstNameChange(firstName="2")
    # app.session.profileLogout()
    time.sleep(5)
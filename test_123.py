import time
import pytest
from groupFTTBlogin import Group
from application import Application


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
    app.VODassetPageBigPlayClick()
    app.loginPagePA_Click()
    app.loginPagePA_emailFieldType(Group(FTTBlogin="demo_autotest"))
    app.loginPagePA_passwordType(FTTBpassword="123456")
    app.loginPagePA_loginBittonClick()
    app.VODplayerVolumeOff()
    app.VODplayerPauseClick()
    time.sleep(5)
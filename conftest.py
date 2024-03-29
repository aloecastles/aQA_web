
import pytest
from fixture.application import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.applicationLaunch()
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.applicationLaunch()
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # fixture.applicationLaunch()
        fixture.session.ensure_Logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
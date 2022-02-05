
import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    fixture.applicationLaunch()
    def fin():
        fixture.applicationLaunch()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
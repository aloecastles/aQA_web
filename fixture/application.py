from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from fixture.session import SessionHelper
from fixture.VODplayer import VODplayerHelper
from fixture.profile import ProfileHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.VODplayer = VODplayerHelper(self)
        self.profile = ProfileHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def firstSearchResultOpen(self):
        wd = self.wd
        # open first search result in 1st row
        time.sleep(3)
        wd.find_element(By.CSS_SELECTOR,
                        "#cdk-overlay-0 > vd-sidenav-search > div > div:nth-child(3) > div > div > vd-search-tiles > div > div.tiles-wrapper > div > img").click()

    def searchQuery(self, Query):
        wd = self.wd
        # search query
        wd.find_element(By.CSS_SELECTOR,
                        "#cdk-overlay-0 > vd-sidenav-search > div > div.header > form > div > input").send_keys(Query)

    def searchOpen(self):
        wd = self.wd
        # search button click
        time.sleep(3)
        wd.find_element(By.CSS_SELECTOR,
                        "body > vd-root > vd-navbar > div.nav > div.nav__btn.nav__search > button").click()

    def applicationLaunch(self):
        wd = self.wd
        # app open
        wd.get("https://tv.kyivstar.ua/en")
        wd.maximize_window()

    def destroy(self):
        self.wd.quit()
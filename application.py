from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def VODplayerPauseClick(self):
        wd = self.wd
        # opened VOD page pause(\play) click
        time.sleep(1)
        wd.find_element(By.CLASS_NAME, "btn-play").click()

    def VODplayerVolumeOff(self):
        wd = self.wd
        # opened VOD page volume off in player
        wd.find_element(By.CLASS_NAME, "icon-volume").click()

    def loginPagePA_loginBittonClick(self):
        wd = self.wd
        # login page "login" button click
        wd.find_element(By.CSS_SELECTOR,
                        "#cdk-overlay-1 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > section > div > vd-login-contract-form > div > form > button.btn.btn-primary.btn_login.next-step").click()

    def loginPagePA_passwordType(self, FTTBpassword):
        wd = self.wd
        # login page "Password" field type in
        wd.find_element(By.CLASS_NAME, "login-input_password").send_keys(FTTBpassword)

    def loginPagePA_emailFieldType(self, group):
        wd = self.wd
        # login page "Email or personal account number" field type in
        wd.find_element(By.CSS_SELECTOR,
                        "#cdk-overlay-1 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > section > div > vd-login-contract-form > div > form > vd-form-field:nth-child(1) > div > div.vd-form-field__field-wrap > input").send_keys(group.FTTBlogin)

    def loginPagePA_Click(self):
        wd = self.wd
        # login page personal account button click
        wd.find_element(By.CSS_SELECTOR,
                        "#cdk-overlay-1 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > div > div:nth-child(2)").click()

    def VODassetPageBigPlayClick(self):
        wd = self.wd
        # opened VOD page big play button click
        wd.find_element(By.CSS_SELECTOR,
                        "body > vd-root > div > vd-details-page > vd-vod > div.asset.ng-star-inserted > div > div > div.actions > button").click()

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
        wd.get("https://tv.kyivstar.ua")
        wd.maximize_window()

    def destroy(self):
        self.wd.quit()
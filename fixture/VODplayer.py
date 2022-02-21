from selenium.webdriver.common.by import By
import time

class VODplayerHelper:
    def __init__(self, app):
        self.app = app

    def PauseClick(self):
        wd = self.app.wd
        # opened VOD page pause(\play) click
        time.sleep(1)
        wd.find_element(By.CLASS_NAME, "btn-play").click()

    def VolumeOff(self):
        wd = self.app.wd
        # opened VOD page volume off in player
        wd.find_element(By.CLASS_NAME, "icon-volume").click()



    def CenterButtonPlayClick(self):
        wd = self.app.wd
        # opened VOD page big play button click
        wd.find_element(By.CLASS_NAME,"btn-accent").click()
        # wd.find_element(By.CSS_SELECTOR,"body > vd-root > div > vd-details-page > vd-vod > div.asset.ng-star-inserted > div > div > div.actions > button").click()
from selenium import webdriver
import time
import unittest

from selenium.webdriver.common.by import By


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test1(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)

    def test_test1(self):
        success = True
        wd = self.wd
        wd.get("https://tv.kyivstar.ua")
        wd.maximize_window()
        time.sleep(3)
        wd.find_element(By.CSS_SELECTOR, "body > vd-root > vd-navbar > div.nav > div.nav__btn.nav__search > button").click()
        wd.find_element(By.CSS_SELECTOR, "#cdk-overlay-0 > vd-sidenav-search > div > div.header > form > div > input").send_keys("суперсила")
        time.sleep(3)
        wd.find_element(By.CSS_SELECTOR, "#cdk-overlay-0 > vd-sidenav-search > div > div:nth-child(3) > div > div > vd-search-tiles > div > div.tiles-wrapper > div > img").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
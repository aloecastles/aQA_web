from selenium import webdriver
import time


driver = webdriver.Chrome()


driver.get("https://tv.kyivstar.ua")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_css_selector("body > vd-root > vd-navbar > div.nav > div.nav__btn.nav__search > button").click()


driver.find_element_by_css_selector("#cdk-overlay-0 > vd-sidenav-search > div > div.header > form > div > input").send_keys("суперсила")
time.sleep(3)

driver.find_element_by_css_selector("#cdk-overlay-0 > vd-sidenav-search > div > div:nth-child(3) > div > div > vd-search-tiles > div > div.tiles-wrapper > div > img").click()
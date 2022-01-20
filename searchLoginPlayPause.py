# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome

    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://tv.kyivstar.ua/")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Ввести промокод'])[1]/following::i[1]").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(u"суперсила")
        driver.find_element_by_xpath("//img[contains(@src,'https://cdn-ksvod.kyivstar.ua/content/HLS/VOD/IMAGE2/61b08ae34074819549a68424/IMAGE_2_3_L.jpg')]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Суперсила Київстар ТБ'])[1]/following::button[1]").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-2']/vd-login-rightdrawer/div/div/vd-login-rightdrawer-form/vd-tabs/div/div[2]/button").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("demo_ro2")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='На вашому Smart TV:'])[3]/following::div[6]").click()
        driver.find_element_by_xpath("//div[@id='cdk-overlay-2']/vd-login-rightdrawer/div/div").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='На вашому Smart TV:'])[3]/following::div[6]").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Продовжити перегляд з 00:00:12'])[1]/following::button[3]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

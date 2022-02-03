from selenium.webdriver.common.by import By
from selenium import webdriver

class ProfileHelper:
    def __init__(self, app):
        self.app = app

    def firstNameChangeAdd(self, group):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body > vd-root > div > vd-new-account > div > section > vd-page-user-info > section > form > div > vd-form-field:nth-child(2) > div > div.vd-form-field__field-wrap > input").send_keys(group.FirstName)

    # def EmailChangeAdd(self, firstName):
    #     wd = self.app.wd
    #     wd.find_element(By.CSS_SELECTOR, "body > vd-root > div > vd-new-account > div > section > vd-page-user-info > section > form > div > vd-form-field:nth-child(1) > div > div.vd-form-field__field-wrap > input").send_keys(firstName)

    def buttonSaveClick(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body > vd-root > div > vd-new-account > div > section > vd-page-user-info > section > form > button:nth-child(3)").click()

    def firstNameClear(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body > vd-root > div > vd-new-account > div > section > vd-page-user-info > section > form > div > vd-form-field:nth-child(2) > div > div.vd-form-field__field-wrap > input").clear()
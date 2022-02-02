from selenium.webdriver.common.by import By
from selenium import webdriver

class ProfileHelper:
    def __init__(self, app):
        self.app = app

    def firstNameChange(self, firstName):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "body > vd-root > div > vd-new-account > div > section > vd-page-user-info > section > form > div > vd-form-field:nth-child(2) > div > div.vd-form-field__field-wrap > input").send_keys(firstName)
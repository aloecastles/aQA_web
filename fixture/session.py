from selenium.webdriver.common.by import By

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def loginPagePAfromVOD_loginButtonClick(self):
        wd = self.app.wd
        # login page "login" button click
        wd.find_element(By.CSS_SELECTOR, "#cdk-overlay-1 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > section > div > vd-login-contract-form > div > form > button.btn.btn-primary.btn_login.next-step").click()

    def loginPagePAfromHome_loginButtonClick(self):
        wd = self.app.wd
        # login page "login" button click
        wd.find_element(By.CSS_SELECTOR, "#cdk-overlay-0 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > section > div > vd-login-contract-form > div > form > button.btn.btn-primary.btn_login.next-step").click()

    def loginPagePA_passwordType(self, group):
        wd = self.app.wd
        # login page "Password" field type in
        if group.FTTBpassword is not None:
            wd.find_element(By.CLASS_NAME, "login-input_password").send_keys(group.FTTBpassword)

    def loginPageFromVodPA_emailFieldType(self, group):
        wd = self.app.wd
        # login page "Email or personal account number" field type in
        if group.FTTBlogin is not None:
            wd.find_element(By.CSS_SELECTOR,
                        "#cdk-overlay-1 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > section > div > vd-login-contract-form > div > form > vd-form-field:nth-child(1) > div > div.vd-form-field__field-wrap > input").send_keys(group.FTTBlogin)

    def loginPageFromHomePA_emailFieldType(self, group):
        wd = self.app.wd
        # login page "Email or personal account number" field type in
        if group.FTTBlogin is not None:
            wd.find_element(By.CSS_SELECTOR, "#cdk-overlay-0 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > section > div > vd-login-contract-form > div > form > vd-form-field:nth-child(1) > div > div.vd-form-field__field-wrap > input").send_keys(group.FTTBlogin)

    def loginPageFromVOD_PA_Click(self):
        wd = self.app.wd
        # login page personal account button click
        wd.find_element(By.CSS_SELECTOR, "#cdk-overlay-1 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > div > div:nth-child(2)").click()

    def loginPageFromHome_PA_Click(self):
        wd = self.app.wd
        # login page personal account button click
        wd.find_element(By.CSS_SELECTOR, "#cdk-overlay-0 > vd-login-rightdrawer > div > div > vd-login-rightdrawer-form > vd-tabs > div > div:nth-child(2) > button").click()

    def profileOpen(self):
        wd = self.app.wd
        wd.find_element(By.CLASS_NAME, "profile-link").click()

    def signInOpen(self):
        wd = self.app.wd
        wd.find_element(By.CLASS_NAME, "btn_login").click()

    def profileLogoutClick(self):
        wd = self.app.wd
        wd.find_element(By.CLASS_NAME, "profile-link").click()
        wd.find_element(By.CSS_SELECTOR, "body > vd-root > div > vd-new-account > div > nav > vd-profile-menu > ul > li:nth-child(6)").click()
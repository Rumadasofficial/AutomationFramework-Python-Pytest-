import time

from selenium import webdriver


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_text = "Log in"
    link_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("id", "Email").clear()
        self.driver.find_element("id", "Email").send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("id", "Password").clear()
        self.driver.find_element("id", "Password").send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", "//button[@class='button-1 login-button']").click()

    def clickLogOut(self):
        self.driver.find_element("xpath", "//a[contains(text(),'Logout')]").click()

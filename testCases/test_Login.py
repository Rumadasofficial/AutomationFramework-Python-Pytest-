import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_homePageTitle(self, setup):
        self.logger.info("********Test_001_Login*************")
        self.logger.info("********Verifying Home page title*************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("********Home page title test case is passed*************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********Home page title test case is failed*************")
            assert False

    @pytest.mark.sanity
    def test_loginPage(self, setup):
        self.logger.info("********Verifying Login Test*************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********Login test case is passed*************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_loginPage.png")
            self.driver.close()
            self.logger.error("********Login test case is failed*************")
            assert False


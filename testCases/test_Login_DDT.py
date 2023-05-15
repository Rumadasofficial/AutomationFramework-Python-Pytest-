import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//testdata/TestData.xlsx"
    logger = LogGen.logGen()

    @pytest.mark.regression
    def test_loginPage_DDT(self, setup):
        self.logger.info("********Test_002_DDT_Login*************")
        self.logger.info("********Verifying Login DDT Test*************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        lst_status = []  # Empty list to store status
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.expStatus = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.expStatus == "pass":
                    self.logger.info("********Login test case with valid data is passed*************")
                    self.lp.clickLogOut()
                    lst_status.append("pass")
                elif self.expStatus == "fail":
                    self.logger.info("********Login test case with valid data is failed*************")
                    self.lp.clickLogOut()
                    lst_status.append("fail")
            if act_title != exp_title:
                if self.expStatus == "fail":
                    self.logger.info("********Login test case with invalid data is passed*************")
                    lst_status.append("pass")
                elif self.expStatus == "pass":
                    self.logger.info("********Login test case with invalid data is failed*************")
                    self.lp.clickLogOut()
                    lst_status.append("fail")
        if "fail" not in lst_status:
            self.logger.info("************ Login DDT test case is Passed........*******************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************ Login DDT test case is Failed.......*******************")
            self.driver.close()
            assert False

        self.logger.info("*************End of Login DDT test **********************")
        self.logger.info("*************Completed Test_002_DDT_Login**********************")

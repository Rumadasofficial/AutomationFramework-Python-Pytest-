import time

from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerpage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_004_SearchCustomerByEmail:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("*****************Test_004_SearchCustomerByEmail**************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****************Login Successfully**************************")

        self.logger.info("*****************Starting Search Customer by Email**************************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersmenu()
        time.sleep(3)
        self.addCust.clickOnCustomersMenuItem()

        self.logger.info("*****************Searching Customer by Email**************************")
        searchCust = SearchCustomer(self.driver)
        time.sleep(2)
        searchCust.setEmail("victoria_victoria@nopCommerce.com")
        time.sleep(1)
        searchCust.clickOnSerchbtn()
        status = searchCust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*******************Test_004_SearchCustomerByEmail Finished****************")

        self.driver.close()


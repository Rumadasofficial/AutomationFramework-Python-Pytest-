import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerpage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def random_generator(self, size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def test_addNewCust(self, setup):
        self.logger.info("********Test_003_Add New Customer*************")
        self.logger.info("********Verifying Customer page title*************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login Successfully**********************")

        self.logger.info("***********Starting Add Customer Test**********************")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersmenu()
        time.sleep(3)
        self.addCust.clickOnCustomersMenuItem()
        self.addCust.clickOnAddNew()
        self.logger.info("***********Provide Customer Details**********************")

        self.email = self.random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword('test123')
        self.addCust.setFirstName("Demo")
        self.addCust.setLastName("Customer")
        self.addCust.setGender("Female")
        self.addCust.setDOB("12/12/1990")
        self.addCust.setCompanyName("ABC PVT LTD")
        self.addCust.selectTaxExempt()
        # self.addCust.setCustomerRoles("Registered")
        time.sleep(3)
        self.addCust.setManegerOfVendor("Vendor 1")
        self.addCust.addAdminComm("This is for testing add cust feature")
        self.addCust.clickOnSave()

        self.logger.info("***********Saving Customer Details**********************")
        self.logger.info("***********Add Customer Validation**********************")

        self.msg = self.driver.find_element("tag name", "body").text
        print("Message", self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("*********Added Customer test passed***********")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_addNewCust.png")
            self.logger.info("*********Added Customer test failed***********")
            assert True == False

        self.driver.close()
        self.logger.info("*********Ending Add Customer test***********")

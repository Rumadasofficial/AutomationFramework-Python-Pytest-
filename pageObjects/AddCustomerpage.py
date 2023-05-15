import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class AddCustomer:
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text( ),'Customers')]"
    lnkCustomers_menu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text( ),'Customers')]"
    btn_add_new_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompany_Name_xpath = "//input[@id='Company']"
    chkbox_IsTaxExempt_xpath = "//input[@id='IsTaxExempt']"
    lstbox_Newsletter_xpath = ""
    txtAdmincomment_xpath = "//textarea[@id='AdminComment']"
    drpmgrofVendor_xpath = "//*[@id='VendorId']"
    txtCustomerRoles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']"
    lstitemAdministrator_xpath = "//li[contains(text( ),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text( ),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text( ),'Guests')]]"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersmenu(self):
        self.driver.find_element("xpath", self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element("xpath", self.lnkCustomers_menu_item_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element("xpath", self.btn_add_new_xpath).click()

    def setEmail(self, email):
        self.driver.find_element("xpath", self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element("xpath", self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element("xpath", self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element("xpath", self.txtLastName_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element("xpath", self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self, CompanyName):
        self.driver.find_element("xpath", self.txtCompany_Name_xpath).send_keys(CompanyName)

    def selectTaxExempt(self):
        self.driver.find_element("xpath", self.chkbox_IsTaxExempt_xpath).click()

    def addAdminComm(self, comment):
        self.driver.find_element("xpath", self.txtAdmincomment_xpath).send_keys(comment)

    def clickOnSave(self):
        self.driver.find_element("xpath", self.btnSave_xpath).click()

    def setCustomerRoles(self, role):
        self.driver.find_element("xpath", self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == "Registered":
            self.listitem = self.driver.find_element("xpath", self.lstitemRegistered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element("xpath", self.lstitemAdministrator_xpath)
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element("xpath", "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element("xpath", self.lstitemGuests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element("xpath", self.lstitemRegistered_xpath)
        else:
            self.listitem = self.driver.find_element("xpath", self.lstitemGuests_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click()", self.listitem)

    def setManegerOfVendor(self, value):
        drp = Select(self.driver.find_element("xpath", self.drpmgrofVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element("id", self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element("id", self.rdFemaleGender_id).click()
        else:
            self.driver.find_element("id", self.rdMaleGender_id).click()

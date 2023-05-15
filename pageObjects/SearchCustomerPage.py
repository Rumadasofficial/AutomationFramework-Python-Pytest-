class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFname_id = "SearchFirstName"
    txtLname_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tblSearchResults_id = "customers-grid_wrapper"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody//tr/td"


    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element("id", self.txtEmail_id).clear()
        self.driver.find_element("id", self.txtEmail_id).send_keys(email)

    def setFname(self, Fname):
        self.driver.find_element("id", self.txtFname_id).clear()
        self.driver.find_element("id", self.txtFname_id).send_keys(Fname)

    def setLname(self, Lname):
        self.driver.find_element("id", self.txtLname_id).clear()
        self.driver.find_element("id", self.txtLname_id).send_keys(Lname)

    def clickOnSerchbtn(self):
        self.driver.find_element("id", self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements("xpath", self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements("xpath", self.tableColumn_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element("xpath", self.table_xpath)
            emailId = table.find_element("xpath", "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailId == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfColumns()+1):
            table = self.driver.find_element("xpath", self.table_xpath)
            Name = table.find_element("xpath", "//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if Name == name:
                flag = True
                break
        return flag




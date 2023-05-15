import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser------")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser------")
    else:
        driver = webdriver.Chrome()
        print("Launching default browser------")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI/ hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


################Pytest HTML Report#############################


# IT is hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Ruma'

# IT is hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Platform", None)

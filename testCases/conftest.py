import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService       #To import Firefox browser module (new version)
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.edge.service import Service as EdgeService       #To import edge browser module (new version)
from webdriver_manager.microsoft import EdgeChromiumDriverManager




@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser=="firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser=="edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    return driver


#setup for desired browser:
def pytest_addoption(parser):                   #This will get the value from CLI hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):                           #This will return the browser value to setup method
    return request.config.getoption("--browser")

#=========================================================================================================================
#setup for parallel tests:
#pytest -s -v -n=2 testcase.py      #here n is number of testcases need to run

#=========================================================================================================================

                            ######## pytest HTML report #########################
#add our desired environment setup in HTML report
def pytest_configure(config):
    config._metadata['Project Name']='nop Commerce'
    config._metadata['Module Name'] = 'Customer Login & Title Verification'
    config._metadata['Tester'] = 'Nagarajan Vijayan'


#we can modify/delete from the HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#=========================================================================================================================


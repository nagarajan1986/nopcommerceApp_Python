


import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver


# from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
# from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)



class TestLogin:            #class should be sentence case only

    # baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # useremail = "admin@yourstore.com"
    # password = "admin"

    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):           #function naming should start with test or end with test to run in pytest
        self.logger.info("***************TC_001_HomePage***************")
        self.logger.info("***************Verify HomepageTitle***************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        actual_title=self.driver.title
        print(actual_title)
        # self.driver.close()
        if actual_title=="Your store. Login":
            assert True
            self.logger.info("***************HomePageTitle test is passed***************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_HomePageTitle.png")
            self.logger.error("***************HomePageTitle test is failed***************")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("***************TC_002_LoginPage***************")
        self.logger.info("***************Verify LoginPage***************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        print(act_title)
        # self.driver.close()
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************Login Test is passed***************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_LoginPageTitle.png")
            self.driver.close()
            self.logger.error("***************Login Test is failed***************")
            assert False

        self.logger.info("***************Test Cases Completed Successfully***************")
#
# if __name__ == "__main__":
#     unittest.main()
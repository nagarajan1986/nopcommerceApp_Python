import time
# import unittest

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service as ChromeService       #To import chrome browser module (new version)
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager                     #To import chrome browser module (new version)



class TC_001_Login():
    baseUrl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    logger = LogGen.loggen()

    def test_homePageTitle(self):
        self.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # self.driver.implicitly_wait(30)
        time.sleep(6)
        actual_title = self.driver.title
        print(actual_title)
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***************Login Test is passed***************")
            # self.driver.close()

        else:
            assert False
            self.driver.save_screenshot("C:\\Users\\Admin\\Desktop\\nopcommerce_project\\Screenshots\\Test_LoginPageTitle.png")
            # self.driver.close()
            self.logger.error("***************Login Test is failed***************")



# if __name__ == "__main__":
#     unittest.main()




    # def test_login(self, setup):
    #
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(self.baseUrl)


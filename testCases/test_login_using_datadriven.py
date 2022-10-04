import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
import openpyxl
import utilities.ExcelUtils
import os

from selenium.webdriver.chrome.service import Service as ChromeService  # To import chrome browser module (new version)
from webdriver_manager.chrome import ChromeDriverManager  # To import chrome browser module (new version)


class TestLogin:  # class should be sentence case only
    # Hybrid test cases using DataDriven Testing

    baseURL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\Admin\\Desktop\\nopcommerce_project\\TestData\\data.xlsx"
    logger = LogGen.loggen()
    rows = utilities.ExcelUtils.getRowCount(path, "Sheet1")
    print(rows)

    lst_status=[]               #empty variable

    @pytest.mark.regression
    def test_login(self):
        self.logger.info("***************Verifying LoginTest Using DataDriven***************")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        for r in range(2, self.rows + 1):
            self.username = utilities.ExcelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = utilities.ExcelUtils.readData(self.path, "Sheet1", r, 2)
            self.exp_status = utilities.ExcelUtils.readData(self.path, "Sheet1", r, 3)
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title = self.driver.title
            exp_title="Dashboard / nopCommerce administration"


            if act_title==exp_title:
                if self.exp_status=="Pass":
                    self.logger.info("****** Passed ***********")
                    self.lp.clickLogout()
                    self.lst_status.append("Pass")
                elif self.exp_status=="Fail":
                    self.logger.info("****** Failed ***********")
                    self.lp.clickLogout()
                    self.lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp_status=="Pass":
                    self.logger.info("****** Failed ***********")
                    self.lst_status.append("Fail")
                elif self.exp_status=="Fail":
                    self.logger.info("****** Passed ***********")
                    self.lst_status.append("Pass")

        if "Fail" not in self.lst_status:
            self.logger.info("*********** Login DataDriven Test is Passed **************")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********** Login DataDriven Test is Failed **************")
            self.driver.close()
            assert False


        self.logger.info("**************** This Test Cases is Completed ***************")












#
# if __name__ == "__main__":
#     unittest.main()

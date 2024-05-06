import Data.Data
import random
from Data import Data
from Locators import Locators
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from datetime import date
from datetime import datetime
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class OrangeHR:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=1)

    def boot(self):
        self.driver.get(Data.webData().url)
        self.driver.maximize_window()
        # self.wait.until(ec.url_to_be(Data.webData().url))
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.WebLocators().userNameLocator)))

    def quit(self):
        self.driver.quit()

    def check_exists_by_xpath(self, locator):
        """
        This method verify that web-element is displayed on OrangeHRM website
        :param locator:
        :return:
        """
        if self.driver.find_element(by=By.XPATH, value=locator).is_displayed():
            return True
        else:
            return False

    def enterText(self, locator, textValue):
        element = self.driver.find_element(by=By.XPATH, value=locator)
        element.clear()
        element.send_keys(textValue)

    def clickButton(self, locator):
        self.driver.find_element(by=By.XPATH, value=locator).click()

    def ForgetPassword(self):
        """
        This method verify the forget password functionality for OrangeHRM application
        :return:
        """
        try:
            self.boot()
            for row in range(2, 3):

                self.clickButton(Locators.WebLocators().forgotPasswordLocator)
                # sleep(5)
                self.wait.until(
                    ec.presence_of_element_located((By.XPATH, Locators.WebLocators().ForgotPwdUserNameLocator)))
                username = Data.webData().readData(row, 2)
                self.enterText(Locators.WebLocators().ForgotPwdUserNameLocator, username)
                self.clickButton(Locators.WebLocators().ReesetPwdButtonLocator)
                self.wait.until(ec.url_to_be(Data.webData().pwdResetUrl))

                if self.driver.current_url == Data.webData().pwdResetUrl:
                    print("Password Reset link sent Successfully")
                    Data.webData().writeData(row, 17, "PASSED")
                else:
                    Scenario = Data.webData().readData(row, 4)
                    print("Password Reset Failed")
                    Data.webData().writeData(row, 17, "FAILED")

        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()

    def verifyHeader(self):
        """
        This method verify the header present on orangeHRM application under Admin tab
        :return:
        """
        try:
            self.boot()
            for row in range(3, 4):
                username = Data.webData().readData(row, 2)
                password = Data.webData().readData(row, 3)
                self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.WebLocators().userNameLocator)))
                self.enterText(Locators.WebLocators().userNameLocator, username)
                self.enterText(Locators.WebLocators().passwordLocator, password)
                self.clickButton(Locators.WebLocators().loginButtonLocator)
                sleep(5)
                self.wait.until(
                    ec.presence_of_element_located((By.XPATH, Locators.WebLocators().adminLocator)))

                if self.driver.current_url == Data.webData().dashboardUrl:
                    print("Login is Successfull")
                    self.clickButton(Locators.WebLocators().adminLocator)

                    self.wait.until(
                        ec.presence_of_element_located((By.XPATH, Locators.WebLocators().userManagementLocator)))

                    if self.check_exists_by_xpath(Locators.WebLocators().userManagementLocator) == True:
                        Data.webData().writeData(row, 5, "User Management Tab is displayed")
                        print("User Management Tab is displayed")
                        UM_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 5, "User Management Tab is not displayed")
                        print("User Management Tab is not displayed")
                        UM_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().jobLocator) == True:
                        Data.webData().writeData(row, 6, "Job Tab is displayed")
                        print("Job Tab is displayed")
                        JOB_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 6, "Job Tab is not displayed")
                        print("Job Tab is not displayed")
                        JOB_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().organizationLocator) == True:
                        Data.webData().writeData(row, 7, "Organization Tab is displayed")
                        print("Organization Tab is displayed")
                        Organization_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 7, "Organization Tab is not displayed")
                        print("Organization Tab is not displayed")
                        Organization_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().QualificationsLocator) == True:
                        Data.webData().writeData(row, 8, "Qualifications Tab is displayed")
                        print("Qualifications Tab is displayed")
                        Qualifications_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 8, "Qualifications Tab is not displayed")
                        print("Qualifications Tab is not displayed")
                        Qualifications_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().nationalitiesLocator) == True:
                        Data.webData().writeData(row, 9, "Nationalities Tab is displayed")
                        print("Nationalities Tab is displayed")
                        Nationalities_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 9, "Nationalities Tab is not displayed")
                        print("Nationalities Tab is not displayed")
                        Nationalities_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().corporateBrandingLocator) == True:
                        Data.webData().writeData(row, 10, "Corporate Branding Tab is displayed")
                        print("Corporate Branding Tab is displayed")
                        Corporate_Branding_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 10, "Corporate Branding Tab is not displayed")
                        print("Corporate Branding Tab is not displayed")
                        Corporate_Branding_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().configurationLocator) == True:
                        Data.webData().writeData(row, 11, "Configuration Tab is displayed")
                        print("Configuration Tab is displayed")
                        Configuration_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 11, "Configuration Tab is not displayed")
                        print("Configuration Tab is not displayed")
                        Configuration_flag = "RED"

                    if (UM_flag == "GREEN") and (JOB_flag == "GREEN") and (Organization_flag == "GREEN") and (
                            Qualifications_flag == "GREEN") and (Nationalities_flag == "GREEN") and (
                            Corporate_Branding_flag == "GREEN") and (Configuration_flag == "GREEN"):
                        Data.webData().writeData(row, 17, "PASSED")
                    else:
                        Data.webData().writeData(row, 17, "FAILED")



                else:
                    Scenario = Data.webData().readData(row, 4)
                    if Scenario == "InvalidLogin":
                        print("Login is unsuccessfull")

                    else:
                        Data.webData().writeData(row, 17, "FAILED")


        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()

    def verifyMenu(self):
        """
        This method verify the Menu present on OrangeHRM application
        :return:
        """
        try:
            self.boot()
            for row in range(4, 5):
                username = Data.webData().readData(row, 2)
                password = Data.webData().readData(row, 3)
                self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.WebLocators().userNameLocator)))
                self.enterText(Locators.WebLocators().userNameLocator, username)
                self.enterText(Locators.WebLocators().passwordLocator, password)
                self.clickButton(Locators.WebLocators().loginButtonLocator)
                sleep(5)
                if self.driver.current_url == Data.webData().dashboardUrl:
                    print("Login is Successfull")

                    if self.check_exists_by_xpath(Locators.WebLocators().adminLocator) == True:
                        Data.webData().writeData(row, 5, "Admin Menu is displayed")
                        print("Admin Menu is displayed")
                        AdminMenu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 5, "Admin Menu is not displayed")
                        print("Admin Menu is not displayed")
                        AdminMenu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().PIMLocator) == True:
                        Data.webData().writeData(row, 6, "PIM Menu is displayed")
                        print("PIM Menu is displayed")
                        PIMMenu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 6, "PIM Menu is not displayed")
                        print("PIM Menu is not displayed")
                        PIMMenu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().LeaveLocator) == True:
                        Data.webData().writeData(row, 7, "Leave Menu is displayed")
                        print("Leave Menu is displayed")
                        Leave_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 7, "Leave Menu is not displayed")
                        print("Leave Menu is not displayed")
                        Leave_Menu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().TimeLocator) == True:
                        Data.webData().writeData(row, 8, "Time Menu is displayed")
                        print("Time Menu is displayed")
                        TimeMenu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 8, "Time Menu is not displayed")
                        print("Time Menu is not displayed")
                        TimeMenu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().RecruitmentLocator) == True:
                        Data.webData().writeData(row, 9, "Recruitment Menu is displayed")
                        print("Recruitment Menu is displayed")
                        RecruitmentMenu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 9, "Recruitment Menu is not displayed")
                        print("Recruitment Menu is not displayed")
                        RecruitmentMenu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().MyInfoLocator) == True:
                        Data.webData().writeData(row, 10, "My Info Menu is displayed")
                        print("My Info Menu is displayed")
                        MyInfo_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 10, "My Info Menu is not displayed")
                        print("My Info Menu is not displayed")
                        MyInfo_Menu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().PerformanceLocator) == True:
                        Data.webData().writeData(row, 11, "Performance Menu is displayed")
                        print("Performance Menu is displayed")
                        Performance_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 11, "Performance Menu is not displayed")
                        print("Performance Menu is not displayed")
                        Performance_Menu_flag = "RED"

                        ###########################

                    if self.check_exists_by_xpath(Locators.WebLocators().DashboardLocator) == True:
                        Data.webData().writeData(row, 12, "Dashboard Menu is displayed")
                        print("Dashboard Menu is displayed")
                        Dashboard_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 12, "Dashboard Menu is not displayed")
                        print("Dashboard Menu is not displayed")
                        Dashboard_Menu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().DirectoryLocator) == True:
                        Data.webData().writeData(row, 13, "Directory Menu is displayed")
                        print("Directory Menu is displayed")
                        Directory_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 13, "Directory Menu is not displayed")
                        print("Directory Menu is not displayed")
                        Directory_Menu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().MaintenanceLocator) == True:
                        Data.webData().writeData(row, 14, "Maintenance Menu is displayed")
                        print("Maintenance Menu is displayed")
                        Maintenance_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 14, "Maintenance Menu is not displayed")
                        print("Maintenance Menu is not displayed")
                        Maintenance_Menu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().ClaimLocator) == True:
                        Data.webData().writeData(row, 15, "Claim Menu is displayed")
                        print("Claim Menu is displayed")
                        Claim_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 15, "Claim Menu is not displayed")
                        print("Claim Menu is not displayed")
                        Claim_Menu_flag = "RED"

                    if self.check_exists_by_xpath(Locators.WebLocators().BuzzLocator) == True:
                        Data.webData().writeData(row, 16, "Buzz Menu is displayed")
                        print("Buzz Menu is displayed")
                        Buzz_Menu_flag = "GREEN"
                    else:
                        Data.webData().writeData(row, 16, "Buzz Menu is not displayed")
                        print("Buzz Menu is not displayed")
                        Buzz_Menu_flag = "RED"

                    if (AdminMenu_flag == "GREEN") and (PIMMenu_flag == "GREEN") and (Leave_Menu_flag == "GREEN") and (
                            TimeMenu_flag == "GREEN") and (RecruitmentMenu_flag == "GREEN") and (
                            MyInfo_Menu_flag == "GREEN") and (Performance_Menu_flag == "GREEN") and (
                            Dashboard_Menu_flag == "GREEN") and (Directory_Menu_flag == "GREEN") and (
                            Maintenance_Menu_flag == "GREEN") and (Claim_Menu_flag == "GREEN") and (
                            Buzz_Menu_flag == "GREEN"):
                        Data.webData().writeData(row, 17, "PASSED")
                    else:
                        Data.webData().writeData(row, 17, "FAILED")



                else:
                    Scenario = Data.webData().readData(row, 4)
                    if Scenario == "InvalidLogin":
                        print("Login is unsuccessfull")

                    else:
                        Data.webData().writeData(row, 10, "FAILED")


        except NoSuchElementException as e:
            print(e)
        finally:
            self.quit()

# TC_PIM_01
obj1 = OrangeHR()
obj1.ForgetPassword()

# TC_PIM_02
obj2 = OrangeHR()
obj2.verifyHeader()

# TC_PIM_03
obj3 = OrangeHR()
obj3.verifyMenu()

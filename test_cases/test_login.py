import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.Login_Page import Login_Page


class Test_TC010_Login:
    page_url = "https://fishingbooker.com/auth/login"
    invalid_email = "testmail.com"

    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        act_title = self.driver.title
        exp_title = "Welcome! Log In Here - FishingBooker"
        if act_title == exp_title :
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    def test_title_error_verification(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        act_title = self.driver.title
        exp_title = "Welcome!!! Log In Here - FishingBooker"
        if act_title == exp_title :
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_error_verification.png")
            self.driver.close()
            assert False

    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.lp = Login_Page(self.driver)
        self.lp.enter_username(self.invalid_email)
        self.lp.click_login()
        error_message = self.driver.find_element(By.XPATH, "//div[@class='label label-danger']").text
        print("Error msg:", error_message)
        if "Enter a valid email." in error_message:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_login.png")
            assert False
        self.driver.close()

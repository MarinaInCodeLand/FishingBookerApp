import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.SignUp_Page import SignUp_Page

class Test_TC011_SignUp:
    page_url = "https://fishingbooker.com/auth/signup"
    empty_first_name_input = ""
    empty_last_name_input = ""
    empty_email_input = ""
    empty_password_input = ""

    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        act_title = self.driver.title

        exp_title = "Sign up - FishingBooker"
        if act_title == exp_title :
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    def test_invalid_sign_up(self, setup):
        self.driver = setup
        self.driver.get(self.page_url)
        self.sp = SignUp_Page(self.driver)
        self.sp.enter_first_name(self.empty_first_name_input)
        self.sp.enter_last_name(self.empty_last_name_input)
        self.sp.enter_email_address(self.empty_email_input)
        self.sp.enter_password(self.empty_password_input)
        self.sp.click_sign_up()
        error_message = self.driver.find_element(By.XPATH, "//div[normalize-space()='First Name is required.']").text
        print("Error msg:", error_message)
        if "First Name is required." in error_message:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_sign_up.png")
            assert False
        self.driver.close()

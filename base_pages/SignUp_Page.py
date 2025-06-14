from selenium.webdriver.common.by import By

class SignUp_Page:
    textbox_first_name_id = "first-name"
    textbox_last_name_id = "last-name"
    textbox_email_address_id = "username"
    textbox_password_id = "password"
    button_sign_up_xpath = "//button[@data-testid='auth-submit-button']"

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.ID, self.textbox_first_name_id).clear()
        self.driver.find_element(By.ID, self.textbox_first_name_id).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.ID, self.textbox_last_name_id).clear()
        self.driver.find_element(By.ID, self.textbox_last_name_id).send_keys(last_name)

    def enter_email_address(self, email_address):
        self.driver.find_element(By.ID, self.textbox_email_address_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_address_id).send_keys(email_address)

    def enter_password(self, email_address):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(email_address)

    def click_sign_up(self):
        self.driver.find_element(By.XPATH, self.button_sign_up_xpath).click()
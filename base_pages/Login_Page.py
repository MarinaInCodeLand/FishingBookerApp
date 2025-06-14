from selenium.webdriver.common.by import By

class Login_Page:
    textbox_username_id = "username"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
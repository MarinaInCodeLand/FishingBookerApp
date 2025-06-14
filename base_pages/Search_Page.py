from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Search_Page:
    search_next_destination_input_xpath = "//input[@data-testid='search-form-input-field']"
    select_date_input_id = "date-picker"
    group_size_input_id = "group-size-picker-input"
    button_check_availability_xpath = "//a[@data-testid='search-form-check-availability-button']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_your_next_destination(self, destination):
        search_input = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_next_destination_input_xpath)))
        search_input.clear()
        search_input.send_keys(destination)
        time.sleep(2)  # čekanje da se pojave sugestije
        search_input.send_keys(Keys.ARROW_DOWN)
        search_input.send_keys(Keys.ENTER)

    def first_available_day(self, day="25"):
        self.wait.until(EC.element_to_be_clickable((By.ID, self.select_date_input_id))).click()
        time.sleep(1)
        day_button = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//button[@data-day='{day}']")))
        day_button.click()

    def enter_group_size(self, size="2"):
        group_input = self.wait.until(EC.element_to_be_clickable((By.ID, self.group_size_input_id)))
        group_input.send_keys(size)

    def click_check_availability(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_check_availability_xpath))).click()

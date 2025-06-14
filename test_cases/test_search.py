import pytest
from selenium import webdriver
from base_pages.Search_Page import Search_Page

class Test_TC001_Search_Valid_Destination:

    def test_search_valid_destination(self, setup):
        driver = setup
        driver.get("https://fishingbooker.com/")

        search_page = Search_Page(driver)

        # 1. Enter the destination
        search_page.enter_your_next_destination("Belgrade")

        # 2. Select the first available date (e.g., 25)
        search_page.first_available_day(day="25")

        # 3. Enter the number of people (e.g., 2)
        #search_page.enter_group_size("2")

        # 4. Click the "Check availability" button
        search_page.click_check_availability()

        # 5. Verify that the page was redirected to the results page.
        assert "search" in driver.current_url.lower(), "Check availability did not redirect to results page"

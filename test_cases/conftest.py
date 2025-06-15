import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # KORISTI verziju ChromeDriver-a koja odgovara Chrome 115
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(version="115.0.5790.170").install()),
        options=chrome_options
    )

    yield driver
    driver.quit()



import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ne prikazuje prozor browsera
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # koristi tačnu verziju ChromeDriver-a koja je instalirana u GitHub Actions
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(version="116.0.5845.96").install()),
        options=chrome_options
    )
    driver.maximize_window()
    yield driver
    driver.quit()

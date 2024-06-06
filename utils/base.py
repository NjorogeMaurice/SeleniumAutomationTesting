import pytest
import yaml
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    # Load config
    with open("config/config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config["url"])

    request.cls.driver = driver
    request.cls.config = config

    yield

    driver.quit()

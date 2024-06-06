from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")
        self.home_page_element = (By.ID, "homePageElement")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_page_element)
        )

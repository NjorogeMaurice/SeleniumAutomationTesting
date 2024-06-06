import pytest
from pages.loginPage import LoginPage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login_valid(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username(self.config["username"])
        login_page.enter_password(self.config["password"])
        login_page.click_login()

        assert login_page.is_logged_in(), "Login failed"

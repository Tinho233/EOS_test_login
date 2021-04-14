import time

import pytest

from pages.base_page import BasePage
from pages.home_page import HomePage
from settings import *
from user import User


class TestLogin:

    def test_registration(self, driver):
        verification_email = "Пожалуйста, верифицируйте свою электронную почту"
        home = HomePage(driver)
        home.go_to(BASE_URL)
        home.login(User.FIRST_NAME, User.LAST_NAME, User.EMAIL, User.PASSWORD)
        verification_email_actual = home.get_verification_email_message()
        assert verification_email == verification_email_actual,\
            f"Email verification actual - {verification_email_actual}, expected - {verification_email}"

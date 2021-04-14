import time

import pytest

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

    def test_valid_login(self, driver):
        user_email = User.EMAIL
        home = HomePage(driver)
        home.go_to(BASE_URL)
        home.click_sign_in_login()
        home.enter_email(User.EMAIL)
        home.enter_password(User.PASSWORD)
        home.click_sign_in_button()
        home.click_sidebar_user_menu()
        user_email_actual = home.get_user_email_info()
        assert user_email == user_email_actual, \
            f"User email actual - {user_email_actual}, expected - {user_email}"

import pytest
from pages.home_page import HomePage
from settings import *
from user import User


class TestLogin:

    def test_registration(self, driver):
        verification_email = "Пожалуйста, верифицируйте свою электронную почту"
        home = HomePage(driver)
        home.go_to(BASE_URL)
        home.login(User.FIRST_NAME, User.LAST_NAME, User.RANDOM_EMAIL, User.PASSWORD)
        verification_email_actual = home.get_verification_email_message()
        assert verification_email == verification_email_actual,\
            f"Email verification actual - {verification_email_actual}, expected - {verification_email}"

    def test_valid_login(self, driver):
        home = HomePage(driver)
        home.go_to(BASE_URL)
        home.click_sign_in_login()
        home.enter_email(User.EMAIL)
        home.enter_password(User.PASSWORD)
        home.click_sign_in_button()
        home.click_sidebar_user_menu()
        assert home.wait_user_mail(User.EMAIL), f"User mail {User.EMAIL} not found"

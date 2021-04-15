import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import HomePageLocators as locs
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):

    def enter_first_name(self, first_name):
        self.enter_text(locs.first_name_input, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(locs.last_name_input, last_name)

    def enter_email(self, email):
        self.enter_text(locs.email_input, email)

    def enter_password(self, password):
        self.enter_text(locs.password_input, password)

    def click_checkbox(self):
        checkbox = self.wait_element(locs.checkbox_confirm)
        ActionChains(self.driver).move_to_element(checkbox).click(checkbox).perform()

    def click_sign_up_button(self):
        self.wait_element(locs.sign_up_button).click()

    def login(self, first_name, last_name, email, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_checkbox()
        time.sleep(1)
        self.click_sign_up_button()

    def get_verification_email_message(self):
        return self.wait_element(locs.verification_email_message).text

    def click_sign_in_login(self):
        self.wait_element(locs.sign_in).click()

    def click_sign_in_button(self):
        self.wait_element(locs.sign_in_button).click()

    def click_sidebar_user_menu(self):
        self.wait_element(locs.sidebar_user_menu).click()

    def wait_user_mail(self, text):
        return self.wait_until_element_has_text(locs.email_user_info, text)

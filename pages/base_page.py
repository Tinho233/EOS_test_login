from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from settings import EXPLICIT_TIMEOUT


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def wait_element(self, locator: str, condition=ec.presence_of_element_located, timeout=EXPLICIT_TIMEOUT,
                     by=By.CSS_SELECTOR) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(condition((by, locator)))

    def enter_text(self, locator: str, text: str, timeout=EXPLICIT_TIMEOUT):
        element = self.wait_element(locator, ec.element_to_be_clickable, timeout)
        element.clear()
        element.send_keys(text)

    def wait_until_element_has_text(self, locator: str, text, timeout=EXPLICIT_TIMEOUT, by=By.CSS_SELECTOR):
        try:
            WebDriverWait(self.driver, timeout).until(ec.text_to_be_present_in_element((by, locator), text))
            return True
        except TimeoutException:
            return False

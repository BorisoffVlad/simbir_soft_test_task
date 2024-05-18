from enum import Enum

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser: WebDriver, path="login"):
        super().__init__(browser, path)

    def open_page(self):
        with allure.step(f"Открываем страницу {self.url}"):
            self.browser.get(self.url)

    def click_customer_login(self):
        with allure.step("Кликаем на кнопку Customer Login"):
            self.click_element(locator=LoginPageLocators.CUSTOMER_LOGIN_BUTTON.value)


class LoginPageLocators(Enum):
    CUSTOMER_LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "div:nth-of-type(1) > .btn.btn-lg.btn-primary",
    )

from enum import Enum

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class CustomerPage(BasePage):
    def open_page(self):
        pass

    def __init__(self, browser: WebDriver, path="customer"):
        super().__init__(browser, path)

    def choose_customer_by_name(self, name):
        with allure.step(f"В выпадающем списке выбираем {name}"):
            customers_list = self.find_element(
                locator=CustomerPageLocators.YOUR_NAME_FIELD.value
            )
            select = Select(customers_list)
            select.select_by_visible_text(name)

    def click_login_button(self):
        with allure.step("Кликаем на кнопку Login"):
            self.click_element(locator=CustomerPageLocators.LOGIN_BUTTON.value)


class CustomerPageLocators(Enum):
    YOUR_NAME_FIELD = (By.CSS_SELECTOR, "select#userSelect")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "form[role='form'] > .btn.btn-default")

from enum import Enum

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, browser: WebDriver, path="account"):
        super().__init__(browser, path)

    def open_page(self):
        pass

    def click_transactions_button(self):
        with allure.step("Кликаем на кнопку Transactions"):
            self.click_element(locator=AccountPageLocators.TRANSACTIONS_BUTTON.value)

    def click_deposit_button(self):
        with allure.step("Кликаем на кнопку Deposit"):
            self.click_element(locator=AccountPageLocators.DEPOSIT_BUTTON.value)

    def click_withdraw_button(self):
        with allure.step("Кликаем на кнопку Withdraw"):
            self.click_element(locator=AccountPageLocators.WITHDRAW_BUTTON.value)

    def click_replenish_deposit_button(self):
        with allure.step("Кликаем на кнопку Deposit (добавить депозит)"):
            self.click_element(
                locator=AccountPageLocators.REPLENISH_DEPOSIT_BUTTON.value
            )

    def click_withdraw_deposit_button(self):
        with allure.step("Кликаем на кнопку Withdraw (вывести депозит)"):
            self.click_element(
                locator=AccountPageLocators.WITHDRAW_DEPOSIT_BUTTON.value
            )

    def input_deposited_amount(self, deposited_amount):
        with allure.step(f"Вводим депозит на сумму - {deposited_amount}"):
            self.input_text(
                locator=AccountPageLocators.AMOUNT_TO_BE_DEPOSITED_FIELD.value,
                text=deposited_amount,
            )

    def input_withdrawn_amount(self, withdrawn_amount):
        with allure.step(f"Вводим вычет на сумму - {withdrawn_amount}"):
            self.input_text(
                locator=AccountPageLocators.AMOUNT_TO_BE_WITHDRAW_FIELD.value,
                text=withdrawn_amount,
            )

    def get_information_field_dict(self):
        with allure.step("Получаем данные информационного поля"):
            input_string = self.get_element_inner_text(
                locator=AccountPageLocators.INFORMATION_FIELD.value
            )
            items = [item.strip() for item in input_string.split(",")]
            result = {
                key.strip(): value.strip()
                for key, value in (item.split(":") for item in items)
            }
            return result


class AccountPageLocators(Enum):
    # Кнопки
    TRANSACTIONS_BUTTON = (
        By.CSS_SELECTOR,
        "div:nth-of-type(3) > button:nth-of-type(1)",
    )
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "div:nth-of-type(3) > button:nth-of-type(2)")
    WITHDRAW_BUTTON = (By.CSS_SELECTOR, "div:nth-of-type(3) > button:nth-of-type(3)")
    REPLENISH_DEPOSIT_BUTTON = (By.CSS_SELECTOR, "form[role='form'] > button")
    WITHDRAW_DEPOSIT_BUTTON = (By.CSS_SELECTOR, "form[role='form'] > button")

    # Поля ввода
    AMOUNT_TO_BE_DEPOSITED_FIELD = (
        By.CSS_SELECTOR,
        ".form-control.ng-invalid.ng-invalid-required.ng-pristine.ng-untouched",
    )
    AMOUNT_TO_BE_WITHDRAW_FIELD = (
        By.CSS_SELECTOR,
        ".form-control.ng-invalid.ng-invalid-required.ng-pristine.ng-untouched",
    )

    # Информационные поля
    INFORMATION_FIELD = (
        By.CSS_SELECTOR,
        ".borderM.box.ng-scope.padT20 > div:nth-of-type(2)",
    )

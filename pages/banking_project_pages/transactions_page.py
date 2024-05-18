from enum import Enum

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class TransactionsPage(BasePage):
    def __init__(self, browser: WebDriver, path="listTx"):
        super().__init__(browser, path)

    def open_page(self):
        pass

    def get_transaction_table_data(self):
        with allure.step("Получаем данные таблицы с транзакциями"):
            return self.get_element_inner_text(
                locator=TransactionsPageLocators.TRANSACTION_TABLE.value
            )


class TransactionsPageLocators(Enum):
    TRANSACTION_TABLE = (By.CSS_SELECTOR, ".table.table-bordered.table-striped")

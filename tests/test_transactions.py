import allure
import pytest

from utils import validators, csv_utils, deposit_utils
from pages.banking_project_pages.account_page import AccountPage
from pages.banking_project_pages.customer_page import CustomerPage
from pages.banking_project_pages.login_page import LoginPage
from pages.banking_project_pages.transactions_page import TransactionsPage


class TestTransactions:
    @allure.title("Проверка баланса")
    @allure.description("Проверка баланса после пополнения и вывода депозита")
    def test_check_balance(self, setup_pages_fixture):
        # Arrange
        (
            login_page,
            customer_page,
            account_page,
            customer_name,
            deposit,
        ) = setup_pages_fixture

        expected_balance = 0

        # Act
        login_page.open_page()
        login_page.click_customer_login()

        customer_page.choose_customer_by_name(customer_name)
        customer_page.click_login_button()

        account_page.click_deposit_button()
        account_page.input_deposited_amount(deposit)
        account_page.click_replenish_deposit_button()
        account_page.wait_timeout()

        account_page.click_withdraw_button()
        account_page.input_withdrawn_amount(deposit)
        account_page.click_withdraw_deposit_button()
        information_field_dict = account_page.get_information_field_dict()
        actual_balance = int(information_field_dict["Balance"])

        # Assert
        validators.assert_equals(
            expected=expected_balance,
            actual=actual_balance,
            message=f"Ожидаемое значение поля Balance - {expected_balance}."
            f" Фактическое значение поля Balance - {actual_balance}",
        )

    @allure.title("Проверка наполнения таблицы транзакциями")
    @allure.description(
        "Проверка наполнения таблицы транзакциями после пополнения и вывода депозита"
    )
    def test_check_transactions_table(self, browser, setup_pages_fixture):
        # Arrange
        transactions_page = TransactionsPage(browser)

        (
            login_page,
            customer_page,
            account_page,
            customer_name,
            deposit,
        ) = setup_pages_fixture

        transaction_credit = "Credit"
        transaction_debit = "Debit"

        # Act
        login_page.open_page()
        login_page.click_customer_login()

        customer_page.choose_customer_by_name(customer_name)
        customer_page.click_login_button()

        account_page.click_deposit_button()
        account_page.input_deposited_amount(deposit)
        account_page.click_replenish_deposit_button()
        account_page.wait_timeout()

        account_page.click_withdraw_button()
        account_page.input_withdrawn_amount(deposit)
        account_page.click_withdraw_deposit_button()

        account_page.wait_timeout()
        account_page.click_transactions_button()
        transactions_table_sting = transactions_page.get_transaction_table_data()

        csv_utils.attach_csv_file_to_allure_report(transactions_table_sting)

        # Assert
        validators.check_substring(
            substring=transaction_credit,
            string=transactions_table_sting,
            message=f"Строка {transaction_credit} отсутствует в строке {transactions_table_sting}.",
        )
        validators.check_substring(
            substring=transaction_debit,
            string=transactions_table_sting,
            message=f"Строка {transaction_debit} отсутствует в строке {transactions_table_sting}.",
        )


@pytest.fixture(scope="function")
def setup_pages_fixture(browser):
    login_page = LoginPage(browser)
    customer_page = CustomerPage(browser)
    account_page = AccountPage(browser)
    customer_name = "Harry Potter"
    deposit = deposit_utils.get_deposit()

    return (
        login_page,
        customer_page,
        account_page,
        customer_name,
        deposit,
    )

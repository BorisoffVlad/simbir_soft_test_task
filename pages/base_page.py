import time
from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from config import BASE_URL, DEFAULT_TIMEOUT
import allure


class BasePage(ABC):
    def __init__(self, browser: WebDriver, path: str):
        self.browser = browser
        self.url = BASE_URL + path
        self.default_timeout = DEFAULT_TIMEOUT

    @abstractmethod
    def open_page(self):
        with allure.step(f"Открываем страницу {self.url}"):
            pass

    def find_element(self, locator, timeout=DEFAULT_TIMEOUT):
        with allure.step(f"Находим элемент страницы по локатору {locator}"):
            return WebDriverWait(driver=self.browser, timeout=timeout).until(
                expected_conditions.presence_of_element_located(locator)
            )

    def click_element(self, locator, timeout=DEFAULT_TIMEOUT):
        with allure.step(f"Кликаем на элемент страницы по локатору {locator}"):
            element = self.find_element(locator, timeout)
            element.click()

    def input_text(self, locator, text, timeout=DEFAULT_TIMEOUT):
        with allure.step(f"Вводим {text} в элемент страницы по локатору {locator}"):
            element = self.find_element(locator=locator, timeout=timeout)
            element.clear()
            element.send_keys(text)

    def get_element_text(self, locator, timeout=DEFAULT_TIMEOUT):
        with allure.step(f"Получаем текст элемента страницы по локатору {locator}"):
            element = self.find_element(locator, timeout)
            return element.text

    def scroll_to_element(self, locator):
        with allure.step(f"Скроллим к элементу с локатором {locator}"):
            element = self.browser.find_element(*locator)
            self.browser.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(DEFAULT_TIMEOUT)
            return element

    def scroll_to_element_and_click(self, locator):
        with allure.step(
            f"Скроллим к элементу с локатором {locator} и кликаем на него"
        ):
            self.scroll_to_element(locator).click()

    def scroll_to_element_and_input_text(self, locator, text):
        with allure.step(f"Скроллим к элементу с локатором {locator} и вводим текст"):
            el = self.scroll_to_element(locator)
            el.clear()
            el.send_keys(text)

    def get_element_property(self, locator, property_name):
        with allure.step(
            f"Получение property = {property_name} элемента с локатором {locator}"
        ):
            el = self.find_element(locator=locator)
            property_data = el.get_attribute(property_name)
            return property_data

    def get_element_inner_text(self, locator):
        with allure.step(f"Получение innerText элемента с локатором {locator}"):
            inner_text = self.get_element_property(
                locator=locator, property_name="innerText"
            )
            return inner_text

    def wait_timeout(self):
        time.sleep(self.default_timeout)

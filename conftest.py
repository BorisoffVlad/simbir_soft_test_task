import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default=False)
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless")
        browser = webdriver.Remote(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        browser = webdriver.Remote(options=options)
    else:
        raise ValueError("Браузер должен быть одним из: chrome, firefox")
    yield browser
    browser.quit()

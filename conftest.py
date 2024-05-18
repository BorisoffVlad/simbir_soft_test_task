import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default=False)


@pytest.fixture(scope="function")
def browser(request):
    headless = request.config.getoption("--headless")
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    if headless:
        options.add_argument("--headless")
    chrome_service = Service(
        ChromeDriverManager(cache_manager=DriverCacheManager(valid_range=180)).install()
    )
    browser = webdriver.Chrome(options=options, service=chrome_service)

    browser.set_page_load_timeout(10)
    yield browser
    browser.delete_all_cookies()
    browser.quit()

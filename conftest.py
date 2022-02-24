import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from pages.auth_page import AuthPage


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use headless if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1650,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    page = AuthPage(driver)
    page.email = 'ddsvyatov1'
    page.password = 'Asdwsx12!'
    page.btn.click()
    yield driver
    driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from pages.auth_page import AuthPage
from pages.auth_page import AuthPageProduct
import allure
import uuid

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Используйте headless если ван не нужно использовать интерфейс
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options, request):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    yield driver
    # Этот код будет исполнятся после каждого теста

    if request.node.rep_call.failed:
        # Произвести скриншот если тест упал
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            # Призвести скриншот для локальной отладки
            driver.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # Прикрепить скриншот в отчет Allure
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)

            # Для комфортого фикса:
            print('URL: ', driver.current_url)
            print('Browser logs:')
            for log in driver.get_log('browser'):
                print(log)

        except:
            pass # Если нужно игнорировать какие либо ошибки

def get_test_case_docstring(item):
    """ Эта функция получает строку названия теста из тесткейса и форматирует ее.
        чтобы отображать эту строку документации вместо имени тестовой функции в отчетах.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name



def pytest_itemcollected(item):
    """ Эта функция на лету изменяет названия тест кейсов
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ Эта функция изменяет название
        когда мы используем --collect-only parameter для pytest (чтобы получить полный список всех существующих тестов).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # Если в тест кейсе есть док строко и нам нужно изменить имя на указанное
            # Это строка для более удобного отчета
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')


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

@pytest.fixture(scope='function')
def setup_product(request, get_webdriver):
    driver = get_webdriver
    if request.cls is not None:
        request.cls.driver = driver
    page = AuthPageProduct(driver)
    page.email = 'ddsvyatov1'
    page.password = 'Asdwsx12!'
    page.btn.click()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
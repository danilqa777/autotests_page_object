from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, driver, url=''):
        url = 'https://stage.prodboard.mts.ru/preset/external'
        super().__init__(driver, url)

    email = WebElement(id='username')

    password = WebElement(id='password')

    btn = WebElement(class_name='btn')


class AuthPageProduct(WebPage):

    def __init__(self, driver, url=''):
        url = 'https://stage.prodboard.mts.ru/preset/external/product/BI_60/main-info'
        super().__init__(driver, url)

    email = WebElement(id='username')

    password = WebElement(id='password')

    btn = WebElement(class_name='btn')

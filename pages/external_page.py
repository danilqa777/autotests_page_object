import os
from pages.base import WebPage
from pages.elements import ManyWebElements
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://stage.prodboard.mts.ru/preset/external'

        super().__init__(driver, url)

    # Открытая строка поиска
    search = WebElement(css_selector='.productSearchInput .input')

    # Закрытая строка поиска
    search1 = WebElement(class_name='productSearchInput')

    # Счетчик продуктов
    caunt_PG = WebElement(css_selector='#Governance .counter')

    # Крестик на строке поиска
    closed = WebElement(class_name='suffixIcon')

    # Название одного продукта из блока
    product_title = WebElement(css_selector='.productList .header')

    # Названия в блоках продуктов
    products_titles = ManyWebElements(css_selector='.productList .header')

    # Категории продуктов
    categories = ManyWebElements(css_selector='.categoryNavigation .productsCategoryNavigation .name')

    # кнопка "Показать все" для категорий продуктов
    showmore = WebElement(class_name='showMore')

    # Категория продуктов Product Governance
    category_PG = WebElement(xpath='//*[@id="ProductCategories"]/div[1]')

    # Категория продуктов Мтс банк(Базовае)
    category_MTSBank = WebElement(xpath='//*[@id="ProductCategories"]/div[2]')

    # Категория продуктов Легкий старт
    category_ezstart = WebElement(xpath='//*[@id="ProductCategories"]/div[3]')

    # Категория продуктов Телеком(Базовае)
    category_telecom = WebElement(xpath='//*[@id="ProductCategories"]/div[4]')

    # Категория продуктов Партнерские
    category_partner = WebElement(xpath='//*[@id="ProductCategories"]/div[5]')

    # Категория продуктов Big Data
    category_bigdata = WebElement(xpath='//*[@id="ProductCategories"]/div[6]')

    # Категория продуктов МТС ИИ
    category_mtsII = WebElement(xpath='//*[@id="ProductCategories"]/div[7]')

    # Категория продуктов Сайты
    category_sites = WebElement(xpath='//*[@id="ProductCategories"]/div[8]')

    # Категория продуктов Другое
    category_other = WebElement(xpath='//*[@id="ProductCategories"]/div[9]')

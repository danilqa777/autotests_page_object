#!/usr/bin/python3
# -*- encoding=utf8 -*-

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
    caunt = WebElement(class_name='badgeValue')

    # Крестик на строке поиска
    closed = WebElement(class_name='suffixIcon')

    # Название одного продукта из блока
    product_title = WebElement(css_selector='.productList .header')

    # Названия в блоках продуктов
    products_titles = ManyWebElements(css_selector='.productList .header')

    # Категории продуктов
    categories: str = ManyWebElements(css_selector='.categories .category')

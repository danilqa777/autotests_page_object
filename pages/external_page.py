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

    # Крестик на строке поиска
    closed = WebElement(class_name='suffixIcon')

    # Название одного продукта из блока
    product_title = WebElement(css_selector='.productList .header')

    # Кирпичи продуктов
    products = ManyWebElements(class_name='productItem')

    # Заголовок продукта внутри карточки
    title_in_prod = WebElement(css_selector='.productHeader .name')

    # Названия в блоках продуктов
    products_titles = ManyWebElements(css_selector='.productList .header')

    # Категории продуктов
    categories = ManyWebElements(css_selector='.categoryNavigation .productsCategoryNavigation .name')

    # ______________________________________________________________________________________________________________________________

    # Категория продуктов Product Governance --------------------
    category_PG = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[1]/a')

    # Заголовок категории Product Governance
    category_title_PG = WebElement(id='Governance')

    # Категория продуктов Легкий старт --------------------
    category_ezstart = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[2]/a')

    # Заголовок категории Легкий старт
    category_title_ezstart = WebElement(id='Lightstart')

    # Категория продуктов Мтс банк(Базовае) --------------------
    category_MTSBank = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[3]/a')

    # Заголовок категории Мтс банк(Базовае)
    category_title_MTSBank = WebElement(id='Bank')

    # Категория продуктов Телеком(Базовае) --------------------
    category_telecom = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[4]/a')

    # Заголовок категории Телеком(Базовае)
    category_title_telecom = WebElement(id='Telecom')

    # Категория продуктов Партнерские --------------------
    category_partner = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[5]/a')

    # Заголовок категории Партнерские
    category_title_partner = WebElement(id='Partner')

    # Категория продуктов Big Data --------------------
    category_bigdata = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[6]/a')

    # Заголовок категории Big Data
    category_title_bigdata = WebElement(id='Bigdata')

    # Категория продуктов МТС ИИ --------------------
    category_mtsII = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[7]/a')

    # Заголовок категории МТС ИИ
    category_title_mtsII = WebElement(id='AI')

    # Категория продуктов Сайты --------------------
    category_sites = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[8]/a')

    # Заголовок категории Сайты
    category_title_sites = WebElement(id='Site')

    # Категория продуктов Другое --------------------
    category_other = WebElement(xpath='//*[@id="filtersBar"]/div/div[1]/div[9]/a')

    # Заголовок категории Другое
    category_title_other = WebElement(id='Other')

    #______________________________________________________________________________________________________________________________

    # Фильтр Рынок
    filter_market = WebElement(xpath='//*[@id="filtersBar"]/div/div[2]/div[1]/div[1]/div[2]/div/div')

    # Параметр B2B в фильтре рынок
    b2b = WebElement(xpath='//*[@id="mts-portal-output"]/div[7]/div/div/div[3]')

    # Чипс выбранного фильтра
    filter_chips = WebElement(class_name='selectedValue')

    # Первый по счету статус
    status_item = WebElement(class_name='productStatusItem')

    # Кнопка Добавить продукт
    add_product = WebElement(xpath='//*[@id="filtersBar"]/div/div[3]/div[2]/div[1]')

    # Кнопка добавления Внешнего продукта
    add_ext = WebElement(link_text='Внешний')

    # Кнопка добавления Внешнего продукта
    add_int = WebElement(link_text='Внутренний')

    # Кнопка добавления Внешнего продукта
    add_tech = WebElement(link_text='Технологический')



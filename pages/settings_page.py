import os
from pages.base import WebPage
from pages.elements import ManyWebElements
from pages.elements import WebElement

class SettingsPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://stage.prodboard.mts.ru/preset/external'

        super().__init__(driver, url)


    # Значек шестеренки
    gear = WebElement(class_name='settingsIcon')

    # Настройки главной страници
    mainpage_settings = WebElement(xpath='//*[@id="mts-portal-output"]/div[3]/div/div/div[1]/a/div')

    # Настройки страницы продукта
    productpage_settings = WebElement(xpath='//*[@id="mts-portal-output"]/div[3]/div/div/div[2]/a/div')

    # Настройки добавления и изменения
    addreplace_settings = WebElement(xpath='//*[@id="mts-portal-output"]/div[3]/div/div/div[3]/a/div')

    # Таб " Категории внешних продуктов "
    categories_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div/div[2]/div')

    # Таб "Фильтры"
    filters_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div/div[3]/div')

    # Таб "Статусы"
    statuses_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div/div[4]/div')

    # Таб "Столбцы excel"
    excel_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div/div[5]/div')

    # Все категории
    checkbox_attrs = ManyWebElements(class_name='mts-toggle__text')

    # Первый по счету чекбокс
    checkbox_attr = WebElement(class_name='.mts-toggle__text')

    # Категории продуктов на главной странице
    categories = ManyWebElements(css_selector='.categories .category')

    # кнопка "Показать все" для категорий продуктов
    showmore = WebElement(class_name='showMore')

    # Статусы на главной странице
    statuses = ManyWebElements(css_selector='.productStatusItem .name')

    # Радоибатон статуса Формарование идеи
    check_idea_form = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[1]/div[1]/div[7]/label/div[2]/p[1]')

    # Таб Ключевые свойства внешних продуктов
    ex_keyprop = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div[2]')

    # Коючевое свойство "Бренд МТС"
    keyprop_mts = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[1]/div[1]/div[16]/label/div[2]/p[1]')

    # Ключевые свойства на станице продукта
    keyprop_cheaps = ManyWebElements(css_selector='.productChips .productChip')

    # Таб свойства внешних продуктов
    ex_prop = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div[3]')

    # Таб Ссылки внешних продуктов
    ex_links = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div[4]')

    # Таб Руководство внешних продуктов
    ex_owners = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[1]/div/div[1]/div[1]/div[5]')








    # Элементы в Drag and Drop
    one_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[1]/div')
    two_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[2]/div')
    three_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[3]/div')
    four_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[4]/div')
    five_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[5]/div')
    six_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[6]/div')
    seven_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[7]/div')
    eight_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[8]/div')
    nine_elem = WebElement(xpath='//*[@id="app"]/div/div/div/div/div[4]/div[2]/div/div/div/div[2]/ul/div/span/li[9]/div')
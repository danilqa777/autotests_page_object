import os
from pages.base import WebPage
from pages.elements import ManyWebElements
from pages.elements import WebElement

class ProductPage(WebPage):

    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://stage.prodboard.mts.ru/preset/external/product/BI_60/main-info'

        super().__init__(driver, url)

    # Таб метрик
    metrics_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[1]/div/div[2]')

    # Таб экосистемных модулей
    eco_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[1]/div/div[3]')

    # Таб атомарных продуктов
    atomic_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[1]/div/div[4]')

    # Таб технологических продуктов
    techno_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[1]/div/div[5]')

    # Таб проектов хайпиреон
    project_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[1]/div/div[6]')

    # Таб документов
    doc_tab = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[1]/div/div[7]')

    # Блок "Руководство" (CСсылки)
    owners = ManyWebElements(css_selector='.owners .link')

    # Блок "Руководство" ( Текст )
    owners_text = ManyWebElements(css_selector='.productOwner .name')

    # Анимация загрузки iframe на странице метрик
    metrics_iframe = WebElement(class_name='mts-loading-abp__item')

    # Текс при отсутвии метрик у продукта на станице метрик
    metrics_iframe_none = WebElement(class_name='messageMetrics')

    # Графики показывающие отображение экосистемных связей
    eco_grafs = WebElement(class_name='indicator')

    # Ссылки на продукты в эко модулях
    eco_prod_links = ManyWebElements(css_selector='.ecoModulesTable .link')

    # Текст при отсутствии экосистемных связей
    eco_error = WebElement(class_name='ecosystemsModules')

    # Открытие первого по счету атомарного продукта
    atom_opening = WebElement(class_name='markerCell')

    # Текст при отсутствии атомарных продуктов
    atomic_none = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[2]/div[4]')

    # Открытие первого по счету технологического продукта
    techno_opening = WebElement(class_name='marker')

    # Текст при отсутствии технологических продуктов
    techno_none = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[2]/div[5]/div/div/div/div/div[1]')

    # Технический лидер технологических продктов
    techno_lead = WebElement(css_selector='.technoProductRow .owner .link')

    # Таблица проектов Hyperion
    hype_table = WebElement(class_name='projectsTable')

    # Текст при отсутствии связанных проектов хайпиреон
    hype_none = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[2]/div[6]/div/div')

    # Таблица документов
    docs_table = WebElement(class_name='mts-table-body__row')

    # Текст при отсутствии документов у продукта
    docs_none = WebElement(xpath='//*[@id="app"]/div/div/div/div/div/div[3]/div[2]/div[7]/div/div/div')





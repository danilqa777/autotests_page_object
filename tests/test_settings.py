import time
import pytest
from selenium.webdriver.common.keys import Keys
from pages.settings_page import SettingsPage
from pages.elements import WebElement
from selenium.webdriver import ActionChains
from selenium import webdriver


@pytest.mark.usefixtures('setup')
class TestHomePageSettings:

    def test_all_categories(self):
        """ Отображение всех категорий в настройках  """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.mainpage_settings.click()
        time.sleep(3)
        categories_text = ['Big Data', 'Product Governance', 'Другое', 'Легкий старт', 'МТС Банк (базовые)', 'МТС ИИ', 'Партнерские', 'Сайты', 'Телеком (базовые)']
        assert page.checkbox_attrs.get_text() == categories_text

    def test_all_filters(self):
        """ Отображение всех фильтров в настройках  """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.mainpage_settings.click()
        page.filters_tab.click()
        time.sleep(3)
        filters_text = ['Business owner', 'Chief Technology Officer', 'Chief product owner', 'Cтруктурный тип продукта', 'Product owner', 'QBR Memo', 'Senior Product Owner', 'Web, app', 'delta Appstore', 'delta Google play', 'Активность кода в OEBS', 'Атомарный продукт', 'Бизнес модель ЕПП', 'Бизнес-вертикаль', 'Блок', 'Бренд МТС', 'Бриф на рекламу и продвижение', 'Вице-президент','Дашборд продуктовых метрик', 'Детальное описание продукта', 'Достаточность команды (в %)', 'Заявка на экспертизу качества', 'Инициировано закрытие', 'Интеграция экосистемных модулей с Android', 'Интеграция экосистемных модулей с Web', 'Интеграция экосистемных модулей с iOS', 'Использование ЕПП', 'Карточка ОИС', 'Код и описание в HFM Planning', 'Команда в Team', 'Легкий старт', 'Наличие внешних клиентов', 'Наличие выручки', 'Наличие конкурентов', 'Наличие монетизации', 'Направление бизнеса', 'Новый код продукта в Oracle', 'Основной продукт', 'Оценка Appstore', 'Оценка Google play', 'Подтип внешнего продукта', 'Портфель продуктов', 'Признак FIX в HFM', 'Признак Телеком', 'Признак витрины', 'Признак материальности', 'Признак партнерства', 'Причина закрытия', 'Проблема', 'Продуктовая вертикаль', 'Продуктовая услуга', 'Продуктовая цель', 'Публичное описание', 'Разработка договорных документов', 'Решение', 'Рынок', 'Сбор метрик', 'Ссылка на распорядительный документ', 'Стрим', 'Сущность продукта', 'Теги', 'Тестовая характеристика', 'Тип продукта', 'Тип разработки', 'Товарный знак', 'Трайб техлида', 'Уровень QBR', 'Участие гос.сектора', 'Ценности', 'Центр затрат ЦЗ', 'Частотность пользования', 'Численность (план)', 'Численность (факт)', 'ЭК (Web)', 'ЭК (android)', 'ЭК (ios)', 'Экосистемный продукт', 'Экосистемный продуктовый модуль', 'Этап MVP']

        assert page.checkbox_attrs.get_text() == filters_text

    def test_all_statuses(self):
        """ Отображение всех статусов в настройках  """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.mainpage_settings.click()
        page.statuses_tab.click()
        time.sleep(3)
        statuses_text = ['Выведен из КЭ', 'Запуск отменен', 'Запуск пилота', 'Запущен в КЭ', 'Ожидание решения', 'Разработка', 'Формирование идеи']

        assert page.checkbox_attrs.get_text() == statuses_text

    def test_all_excel(self):
        """ Отображение всех столбцов excel в настройках  """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.mainpage_settings.click()
        page.excel_tab.click()
        time.sleep(3)
        excel_text = ['Business owner', 'Chief Technology Officer', 'Chief product owner', 'Cтруктурный тип продукта', 'Product owner', 'QBR Memo', 'Senior Product Owner', 'Web, app', 'delta Appstore', 'delta Google play', 'Активность кода в OEBS', 'Атомарный продукт', 'Бизнес модель ЕПП', 'Бизнес-вертикаль', 'Блок', 'Бренд МТС', 'Бриф на рекламу и продвижение', 'Вице-президент', 'Дата вывода из КЭ', 'Дата запуска', 'Дата запуска пилота', 'Дата окончания пилота', 'Дата разработки', 'Дата формирования идеи', 'Дашборд продуктовых метрик', 'Детальное описание продукта', 'Достаточность команды (в %)', 'Заявка на экспертизу качества', 'Инициировано закрытие', 'Интеграция экосистемных модулей с Android', 'Интеграция экосистемных модулей с Web', 'Интеграция экосистемных модулей с iOS', 'Использование ЕПП', 'Карточка ОИС', 'Категория продукта', 'Код и описание в HFM Planning', 'Команда в Team', 'Легкий старт', 'Название продукта', 'Наличие внешних клиентов', 'Наличие выручки', 'Наличие конкурентов', 'Наличие монетизации', 'Направление бизнеса', 'Новый код продукта в Oracle', 'Описание продукта', 'Основной продукт', 'Оценка Appstore', 'Оценка Google play', 'Подтип внешнего продукта', 'Портфель продуктов', 'Признак FIX в HFM', 'Признак Телеком', 'Признак витрины', 'Признак материальности', 'Признак партнерства', 'Причина закрытия', 'Проблема', 'Продуктовая вертикаль', 'Продуктовая услуга', 'Продуктовая цель', 'Публичное описание', 'Разработка договорных документов', 'Решение', 'Рынок', 'Сбор метрик', 'Ссылка на распорядительный документ', 'Статус', 'Стрим', 'Сущность продукта', 'Теги', 'Тестовая характеристика', 'Тип продукта', 'Тип разработки', 'Товарный знак', 'Трайб техлида', 'Уровень QBR', 'Участие гос.сектора', 'Ценности', 'Центр затрат ЦЗ', 'Частотность пользования', 'Численность (план)', 'Численность (факт)', 'ЭК (Web)', 'ЭК (android)', 'ЭК (ios)', 'Экосистемный продукт', 'Экосистемный продуктовый модуль', 'Этап MVP']
        assert page.checkbox_attrs.get_text() == excel_text

    def test_on_off_categories(self):  # Не работает тк пока не оптимизированны настройки
        """ Отключение и смена мест категорий в настройках  """

        page = SettingsPage(self.driver)
        page.showmore.click()
        time.sleep(3)
        assert page.categories.get_text() == ['Product Governance100', 'МТС Банк (базовые)30', 'Легкий старт26', 'Телеком (базовые)26', 'Партнерские19', 'Big Data4', 'МТС ИИ1', 'Сайты4', 'Другое22']
        page.gear.click()
        page.mainpage_settings.click()
        page.checkbox_attr.click()
        page.go_back()
        page.showmore.click()
        assert page.categories.get_text() == ['Product Governance100', 'МТС Банк (базовые)30', 'Легкий старт26', 'Телеком (базовые)26', 'Партнерские19', 'МТС ИИ1', 'Сайты4', 'Другое22']
        page.gear.click()
        page.mainpage_settings.click()
        page.nine_elem.chain(650, 370)
        page.go_back()
        page.showmore.click()
        assert page.categories.get_text() == ['Product Governance100', 'МТС Банк (базовые)30', 'Легкий старт26', 'Телеком (базовые)26', 'Партнерские19', 'Big Data4', 'МТС ИИ1', 'Сайты4', 'Другое22']


    def test_on_off_statuses(self):   # Не работает тк пока не оптимизированны настройки
        """ Отключение и смена мест статусов в настройках   """

        page = SettingsPage(self.driver)
        time.sleep(3)
        #assert page.statuses.get_text() == ['Формирование идеи', 'Разработка', 'Запуск пилота', 'Ожидание решения', 'Запущен в КЭ']
        page.gear.click()
        page.mainpage_settings.click()
        page.statuses_tab.click()
        time.sleep(3)
        page.check_idea_form.click()
        page.go_back()
        time.sleep(5)
        #assert page.statuses.get_text() == ['Разработка', 'Запуск пилота', 'Ожидание решения', 'Запущен в КЭ']
        page.gear.click()
        page.mainpage_settings.click()
        page.statuses_tab.click()
        time.sleep(3)
        page.check_idea_form.click()
        time.sleep(3)
        page.seven_elem.chain(650, 210)
        time.sleep(5)
        page.go_back()
        assert page.statuses.get_text() == ['Формирование идеи', 'Разработка', 'Запуск пилота', 'Ожидание решения', 'Запущен в КЭ']

@pytest.mark.usefixtures('setup')
class TestProductPageSettings:
    def test_ex_all_keyprop(self):
        """ Отображение всех ключевых свойств продукта   """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.productpage_settings.click()
        ex_keyprop_text = ['Business owner', 'Chief Technology Officer', 'Chief product owner', 'Cтруктурный тип продукта', 'Product owner', 'QBR Memo', 'Senior Product Owner', 'Web, app', 'delta Appstore', 'delta Google play', 'Активность кода в OEBS', 'Атомарный продукт', 'Бизнес модель ЕПП', 'Бизнес-вертикаль', 'Блок', 'Бренд МТС', 'Бриф на рекламу и продвижение', 'Вице-президент', 'Дата вывода из КЭ', 'Дата запуска', 'Дата запуска пилота', 'Дата окончания пилота', 'Дата разработки', 'Дата формирования идеи', 'Дашборд продуктовых метрик', 'Детальное описание продукта', 'Достаточность команды (в %)', 'Заявка на экспертизу качества', 'Инициировано закрытие', 'Интеграция экосистемных модулей с Android', 'Интеграция экосистемных модулей с Web', 'Интеграция экосистемных модулей с iOS', 'Использование ЕПП', 'Карточка ОИС', 'Категория продукта', 'Код и описание в HFM Planning', 'Команда в Team', 'Легкий старт', 'Наличие внешних клиентов', 'Наличие выручки', 'Наличие конкурентов', 'Наличие монетизации', 'Направление бизнеса', 'Новый код продукта в Oracle', 'Основной продукт', 'Оценка Appstore', 'Оценка Google play', 'Подтип внешнего продукта', 'Портфель продуктов', 'Признак FIX в HFM', 'Признак Телеком', 'Признак витрины', 'Признак материальности', 'Признак партнерства', 'Причина закрытия', 'Проблема', 'Продуктовая вертикаль', 'Продуктовая услуга', 'Продуктовая цель', 'Публичное описание', 'Разработка договорных документов', 'Решение', 'Рынок', 'Сбор метрик', 'Ссылка на распорядительный документ', 'Статус', 'Стрим', 'Сущность продукта', 'Теги', 'Тестовая характеристика', 'Тип продукта', 'Тип разработки', 'Товарный знак', 'Трайб техлида', 'Уровень QBR', 'Участие гос.сектора', 'Ценности', 'Центр затрат ЦЗ', 'Частотность пользования', 'Численность (план)', 'Численность (факт)', 'ЭК (Web)', 'ЭК (android)', 'ЭК (ios)', 'Экосистемный продукт', 'Экосистемный продуктовый модуль', 'Этап MVP']
        assert page.checkbox_attrs.get_text() == ex_keyprop_text

    def test_ex_on_off_keyprop(self):
        """ Отображение всех ключевых свойств продукта   """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.productpage_settings.click()
        page.keyprop_mts.click()
        page.get('https://stage.prodboard.mts.ru/preset/external/product/BI_60/main-info')
        assert page.keyprop_cheaps.get_text() == ['Внешний', 'B2C B2B', 'Легкий старт', 'Сбор метрик']
        page.go_back()
        time.sleep(2)
        page.keyprop_mts.click()
        time.sleep(3)
        page.five_elem.chain(1500, 203)
        time.sleep(3)
        page.get('https://stage.prodboard.mts.ru/preset/external/product/BI_60/main-info')
        page.wait_page_loaded()
        assert page.keyprop_cheaps.get_text() == ['Внешний', 'B2C B2B', 'Легкий старт', 'Сбор метрик']

    def test_ex_on_off_k123123123123123123123123eyprop(self):
        """ О123123   """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.productpage_settings.click()
        page.ex_links.click()
        time.sleep(3)
        page.seven_elem.drag_marker_on_map(800, 207)

        time.sleep(5)


    def test_ex_all_prop(self):
        """ Отображение всех свойств продукта    """

        page = SettingsPage(self.driver)

        page.gear.click()
        page.productpage_settings.click()
        page.ex_prop.click()
        time.sleep(3)
        ex_keyprop_text = ['Business owner', 'Chief Technology Officer', 'Chief product owner', 'Cтруктурный тип продукта', 'Product owner', 'QBR Memo', 'Senior Product Owner', 'Web, app', 'delta Appstore', 'delta Google play', 'Активность кода в OEBS', 'Атомарный продукт', 'Бизнес модель ЕПП', 'Бизнес-вертикаль', 'Блок', 'Бренд МТС', 'Бриф на рекламу и продвижение', 'Вице-президент', 'Дата вывода из КЭ', 'Дата запуска', 'Дата запуска пилота', 'Дата окончания пилота', 'Дата разработки', 'Дата формирования идеи', 'Дашборд продуктовых метрик', 'Детальное описание продукта', 'Достаточность команды (в %)', 'Заявка на экспертизу качества', 'Инициировано закрытие', 'Интеграция экосистемных модулей с Android', 'Интеграция экосистемных модулей с Web', 'Интеграция экосистемных модулей с iOS', 'Использование ЕПП', 'Карточка ОИС', 'Категория продукта', 'Код и описание в HFM Planning', 'Команда в Team', 'Легкий старт', 'Наличие внешних клиентов', 'Наличие выручки', 'Наличие конкурентов', 'Наличие монетизации', 'Направление бизнеса', 'Новый код продукта в Oracle', 'Основной продукт', 'Оценка Appstore', 'Оценка Google play', 'Подтип внешнего продукта', 'Портфель продуктов', 'Признак FIX в HFM', 'Признак Телеком', 'Признак витрины', 'Признак материальности', 'Признак партнерства', 'Причина закрытия', 'Проблема', 'Продуктовая вертикаль', 'Продуктовая услуга', 'Продуктовая цель', 'Публичное описание', 'Разработка договорных документов', 'Решение', 'Рынок', 'Сбор метрик', 'Ссылка на распорядительный документ', 'Статус', 'Стрим', 'Сущность продукта', 'Теги', 'Тестовая характеристика', 'Тип продукта', 'Тип разработки', 'Товарный знак', 'Трайб техлида', 'Уровень QBR', 'Участие гос.сектора', 'Ценности', 'Центр затрат ЦЗ', 'Частотность пользования', 'Численность (план)', 'Численность (факт)', 'ЭК (Web)', 'ЭК (android)', 'ЭК (ios)', 'Экосистемный продукт', 'Экосистемный продуктовый модуль', 'Этап MVP']
        assert page.checkbox_attrs.get_text() == ex_keyprop_text

import time
import pytest
from pages.product_page import ProductPage

@pytest.mark.usefixtures('setup_product')
class TestMainInfo:

    def test_owners_name(self):
        """ Отображение ФИО в руководстве  """

        page = ProductPage(self.driver)
        assert page.owners_text.get_text() == ['Зиборова Ольга Николаевна', 'Мельникова Елена Андреевна', 'Фролова Ольга Сергеевна', 'Фролова Ольга Сергеевна', 'Фарафонов Владимир Николаевич']

    def test_owners_clickable(self):
        """ Проверка кликабелности ФИО руководства  """

        page = ProductPage(self.driver)
        assert page.owners.is_clickable()

    def test_metrics_iframe(self):
        """ Проверка отображении iframe  """

        page = ProductPage(self.driver)
        page.metrics_tab.click()
        time.sleep(3)
        assert page.metrics_iframe.is_visible()

    def test_metrics_iframe_none(self):
        """ Проверка отображения текста если по продукта не ведется сбор данных iframe  """

        page = ProductPage(self.driver)
        page.get("https://stage.prodboard.mts.ru/preset/internal/product/BI_202/metrics")
        assert page.metrics_iframe_none.get_text() == 'Сбор метрик по данному проекту не ведётся'

    def test_eco_modul(self):
        """ Проверка отображения графиков экосистемных связей  """

        page = ProductPage(self.driver)
        page.eco_tab.click()
        assert page.eco_grafs.is_visible()

    def test_eco_modul_error(self):
        """ Проверка корректности текста если нет экосистемных связей  """

        page = ProductPage(self.driver)
        page.get("https://stage.prodboard.mts.ru/preset/internal/product/BI_202/metrics")
        page.eco_tab.click()
        assert page.eco_error.get_text() == 'Интеграция с Экосистемными продуктовыми модулями отсутствует'

    def test_eco_prod_links(self):
        """ Проверка кликабельности продуктов в экосистемных модулях  """

        page = ProductPage(self.driver)
        page.eco_tab.click()
        assert page.eco_prod_links.is_clickable()

    def test_open_atomic_link(self):
        """ Изменение ссылки при открытии атомарного продукта  """

        page = ProductPage(self.driver)
        page.atomic_tab.click()
        page.atom_opening.click()
        link = page.get_current_url()
        assert link == 'https://stage.prodboard.mts.ru/preset/external/product/BI_60/atomic?openAtomic=BI_1883'

    def test_open_atomic_PO_closed_text(self):   # Заработает как выйдет 4 спринт
        """ Проверка текста РО во всех атомарных продуктах  """

        page = ProductPage(self.driver)
        page.atomic_tab.click()
        assert page.owners.get_text() == ['ФИО', 'ФИО', 'ФИО', 'ФИО', 'ФИО']

    def test_open_atomic_PO_closed_clickable(self):   # Заработает как выйдет 4 спринт
        """ Проверка кликабелности РО на всех атомарных продуктах  """

        page = ProductPage(self.driver)
        page.atomic_tab.click()
        assert page.owners.is_clickable()

    def test_atomic_error(self):
        """ При отсутсвии атомарных продуктов отображен корректный текст  """

        page = ProductPage(self.driver)
        page.get("https://stage.prodboard.mts.ru/preset/internal/product/BI_202/metrics")
        page.atomic_tab.click()
        assert page.atomic_none.get_text() == '«Гео» не содержит в своем составе атомарные продукты'

    def test_open_techno_link(self):
        """ Изменение ссылки при открытии технологического продукта  """

        page = ProductPage(self.driver)
        page.techno_tab.click()
        page.techno_opening.click()
        time.sleep(3)
        link = page.get_current_url()
        assert link == 'https://stage.prodboard.mts.ru/preset/external/product/BI_60/techno?openTechno=1089'

    def test_open_techno_lead_clickable(self):
        """ Проверка кликабелности РО на всех технологических продуктах  """

        page = ProductPage(self.driver)
        page.techno_tab.click()
        assert page.techno_lead.is_clickable()

    def test_techno_error(self):
        """ При отсутсвии технологических продуктов отображен корректный текст  """

        page = ProductPage(self.driver)
        page.get("https://stage.prodboard.mts.ru/preset/internal/product/BI_1262/main-info")
        page.techno_tab.click()
        assert page.techno_none.get_text() == '«МТС Тестирование» не имеет связей с технологическими продуктами.'

    def test_open_projects(self):
        """ Отображение таблицы проектов Хайпиреон  """

        page = ProductPage(self.driver)
        page.project_tab.click()
        assert page.hype_table.is_visible()

    def test_projects_error(self):
        """ При отсутсвии проектов хайпиреон отображен корректный текст  """

        page = ProductPage(self.driver)
        page.get("https://stage.prodboard.mts.ru/preset/internal/product/BI_202/main-info")
        page.project_tab.click()
        assert page.hype_none.get_text() == 'Нет данных по проектам из Hyperion'

    def test_open_docs(self):
        """ Отображение таблицы документов  """

        page = ProductPage(self.driver)
        page.doc_tab.click()
        time.sleep(2)
        assert page.docs_table.is_visible()

    def test_docs_error(self):
        """ При отсутсвии документов отображен корректный текст  """

        page = ProductPage(self.driver)
        page.get("https://stage.prodboard.mts.ru/preset/internal/product/BI_202/main-info")
        page.doc_tab.click()
        assert page.docs_none.get_text() == 'Документы не прикреплены'
import time
import pytest
from pytest_selenium import driver
from selenium.webdriver.common.keys import Keys
from pages.external_page import MainPage
from pages.elements import WebElement


@pytest.mark.usefixtures('setup')
class TestHomePageSearch:

    def test_serch_normal(self):
        """ Поиск с валидныи названием продукта работает корректно  """

        page = MainPage(self.driver)

        page.search1.click()
        page.search = 'МТС Маркетолог'
        page.search.send_keys('\ue007')
        page.wait_page_loaded()
        assert page.product_title.is_visible()
        # Проверяем что поиск дал результаты согласно введенному значению:
        assert page.product_title.get_text() == 'МТС Маркетолог'


    def test_search_part(self):
        """ Поиск с частичным названием продукта работает корректно  """

        page = MainPage(self.driver)

        page.search1.click()
        page.search = 'марк'
        page.search.send_keys('\ue007')
        page.wait_page_loaded()
        # Проверяем что поиск дал результаты согласно введенному значению:
        assert page.products_titles.get_text() == ['МТС Маркетолог', 'Анализ геоданных (Geointellect)', 'Бизнес маркет', 'Финансовый супермаркет...']

        for title in page.products_titles.get_text():
            msg = 'Wrong product in search "{}"'.format(title)
            assert 'марк' or "Анализ геоданных (Geointellect)" in title.lower(), msg


    def test_search_eng(self):
        """ Поиск английскими букваими названием продукта работает корректно  """

        page = MainPage(self.driver)

        page.search1.click()
        page.search = 'vfhr'
        page.search.send_keys('\ue007')
        page.wait_page_loaded()

        # Проверяем что поиск дал результаты согласно введенному значению:
        assert page.products_titles.get_text() == ['МТС Маркетолог', 'Анализ геоданных (Geointellect)', 'Бизнес маркет', 'Финансовый супермаркет...']

        for title in page.products_titles.get_text():
            msg = 'Wrong product in search "{}"'.format(title)
            assert 'марк' or "Анализ геоданных (Geointellect)" in title.lower(), msg


    def test_search_oracle(self):
        """ Поиск по оракл id продукта работает корректно  """

        page = MainPage(self.driver)

        page.search1.click()
        page.search = 'MAAS'
        page.search.send_keys('\ue007')
        page.wait_page_loaded()

        # Проверяем что поиск дал результаты согласно введенному значению:
        assert page.product_title.get_text() == 'МТС Маркетолог'


    def test_search_closed(self):
        """ Закрытие строки поиска нажатием на крестик  """

        page = MainPage(self.driver)

        page.search1.click()
        page.closed.click()
        page.closed.wait_until_not_visible()

        # Проверяем что строка поиска закрыта:
        assert page.closed.is_clickable() == False
        pass

    def test_search_from_product(self):
        """ Поиск с валидныи из другого продукта  """

        page = MainPage(self.driver)
        page.product_title.click()
        page.title_in_prod.is_visible()
        page.search1.click()
        page.search = 'МТС Тестирование'
        page.search.send_keys('\ue007')
        page.wait_page_loaded()
        time.sleep(5)
        assert page.product_title.is_visible()
        page.product_title.click()
        page.wait_page_loaded()
        page.title_in_prod.is_visible()
        link = page.get_current_url()
        assert link == 'https://stage.prodboard.mts.ru/preset/internal/product/BI_1262/main-info'

    def test_search_FIO(self):
        """ Поиск по ФИО владельца продукта работает корректно  """

        page = MainPage(self.driver)

        page.search1.click()
        page.search = 'Барбетов'
        page.search.send_keys('\ue007')
        page.wait_page_loaded()

        # Проверяем что поиск дал результаты согласно введенному значению:
        assert page.product_title.get_text() == ['Поиск коммерческих потерь в электрических сетях', 'E-sensor']





@pytest.mark.usefixtures('setup')
class TestNavigationBar:

    def test_categori_PG(self):
        """  Переход по категории Product Governance и проверка заголовка на витрине """

        page = MainPage(self.driver)
        assert page.categories.get_text() == ['Product Governance',  'Легкий старт', 'МТС Банк (базовые)', 'Телеком (базовые)', 'Партнерские', 'Big Data', 'МТС ИИ', 'Сайты', 'Другое']
        assert page.category_title_PG.is_visible()
        assert page.category_title_PG.get_text() == 'Product Governance 100'

    def test_categori_ezstart(self):
        """  Переход по категории Легкий старт и проверка заголовка на витрине """

        page = MainPage(self.driver)
        page.category_ezstart.click()
        assert page.category_title_ezstart.is_visible()
        assert page.category_title_ezstart.get_text() == 'Легкий старт 26'

    def test_categori_MTSBank(self):
        """  Переход по категории МТС Банк (базовые) и проверка заголовка на витрине """

        page = MainPage(self.driver)
        page.category_MTSBank.click()
        assert page.category_title_MTSBank.is_visible()
        assert page.category_title_MTSBank.get_text() == 'МТС Банк (базовые) 30'

    def test_categori_telecom(self):
        """  Переход по категории Телеком (базовые) и проверка заголовка на витрине """

        page = MainPage(self.driver)
        page.category_telecom.click()
        assert page.category_title_telecom.is_visible()
        assert page.category_title_telecom.get_text() == 'Телеком (базовые) 26'

    def test_categori_partner(self):
        """  Переход по категории Партнерские и проверка заголовка на витрине """

        page = MainPage(self.driver)
        page.category_partner.click()
        time.sleep(3)
        assert page.category_title_partner.is_visible()
        assert page.category_title_partner.get_text() == 'Партнерские 19'

    def test_categori_mtsII(self):
        """  Переход по категории МТС ИИ и проверка заголовка на витрине """

        page = MainPage(self.driver)
        page.category_mtsII.click()
        assert page.category_title_mtsII.is_visible()
        assert page.category_title_mtsII.get_text() == 'МТС ИИ 1'

    def test_categori_sites(self):
        """  Переход по категории Сайты и проверка заголовка на витрине """

        page = MainPage(self.driver)
        page.category_partner.click()
        assert page.category_title_sites.is_visible()
        assert page.category_title_sites.get_text() == 'Сайты 4'

    def test_categori_other(self):
        """  Переход по категории Другое и проверка заголовка на витрине """

        page = MainPage(self.driver)
        page.category_other.click()
        assert page.category_title_other.is_visible()
        assert page.category_title_other.get_text() == 'Другое 22'

    def test_filters(self):
        """  Проверка корректности работы фильтров на примере фильтра Рынок - B2B """

        page = MainPage(self.driver)
        page.filter_market.click()
        page.b2b.click()
        assert page.filter_chips.is_visible()
        assert page.products.count() == 100

    def test_status(self):
        """  Проверка корректности работы статусов на примере статуса Формирование идеи """

        page = MainPage(self.driver)
        page.status_item.click()
        time.sleep(5)
        assert page.products.count() == 2

    def test_add_ext(self):
        """  Провека отображения и кликабельности кнопки добавления внешнего продукта  """

        page = MainPage(self.driver)
        page.add_product.click()
        assert page.add_ext.is_visible()
        assert page.add_ext.is_clickable()

    def test_add_int(self):
        """  Провека отображения и кликабельности кнопки добавления внутреннего продукта  """

        page = MainPage(self.driver)
        page.add_product.click()
        assert page.add_int.is_visible()
        assert page.add_int.is_clickable()

    def test_add_techno(self):
        """  Провека отображения и кликабельности кнопки добавления технологического продукта  """

        page = MainPage(self.driver)
        page.add_product.click()
        assert page.add_tech.is_visible()
        assert page.add_tech.is_clickable()













#def test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Try to enter "смартфон" with English keyboard:
    page.search = 'cvfhnajy'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 48

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' in title.lower(), msg


#@pytest.mark.xfail(reason="Filter by price doesn't work")
#def test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.

        Note: this test case will fail because there is a bug in
              sorting products by price.
    """

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()

    # Convert all prices from strings to numbers
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    print(all_prices)
    print(sorted(all_prices))

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"


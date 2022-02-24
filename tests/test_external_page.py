import time
import pytest
from pytest_selenium import driver
from selenium.webdriver.common.keys import Keys
from pages.external_page import MainPage
from pages.elements import WebElement


@pytest.mark.usefixtures('setup')
class TestHomePageSearch:

    def test_serch_norman(self):
        """ Поиск с валидныи названием продукта работает корректно  """

        page = MainPage(self.driver)

        page.search1.click()
        page.search = 'МТС Маркетолог'
        page.search.send_keys('\ue007')
        page.wait_page_loaded()
        time.sleep(3)
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


@pytest.mark.usefixtures('setup')
class TestNavigationBar:

    def test_categori(self):

        page = MainPage(self.driver)
        print(page.categories.get_text())









def test_check_wrong_input_in_search(web_browser):
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


@pytest.mark.xfail(reason="Filter by price doesn't work")
def test_check_sort_by_price(web_browser):
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


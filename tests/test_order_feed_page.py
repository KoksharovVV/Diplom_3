import allure
from data import TestDataUrl
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title('Проверка открытия окна с информацие о заказе')
    def test_open_window_with_order_details(self, driver):
        page = OrderFeedPage(driver)
        page.open_page(TestDataUrl.ORDER_FEED_URL)
        page.click_on_order_in_order_feed()
        assert page.find_order_window()

    @allure.title('Проверка обновления счетчика "Выполненно сегодня"')
    def test_update_counter_competed_today(self, driver, log_in):
        page = MainPage(driver)
        page.click_on_order_feed()
        old_counter = page.get_counter_completed_today()
        page.click_on_constructor()
        page.create_order()
        page.click_on_order_feed()
        new_counter = page.get_counter_completed_today()
        assert int(old_counter) < int(new_counter)

    @allure.title('Проверка обновления счетчика "Выполненно за все время"')
    def test_update_counter_competed_for_all_time(self, driver, log_in):
        page = MainPage(driver)
        page.click_on_order_feed()
        old_counter = page.get_counter_completed_for_all_time()
        page.click_on_constructor()
        page.create_order()
        page.click_on_order_feed()
        new_counter = page.get_counter_completed_for_all_time()
        assert int(old_counter) < int(new_counter)

    @allure.title('Проверка попадания нового заказа в ленту заказов')
    def test_find_order_id_after_placing_order(self, driver, log_in):
        page = MainPage(driver)
        id_order = page.create_order()
        page.click_on_order_feed()
        assert page.get_order_in_work()[1:] == id_order

    @allure.title('Проверка отображения заказов из истории заказов в ленте заказов')
    def test_contains_order_history_in_orders_feed(self, driver, log_in):
        page = MainPage(driver)
        page.open_personal_cabinet()
        page.open_history_orders()
        orders_history = page.get_id_orders_from_history()
        page.click_on_order_feed()
        orders_feed = page.get_orders_from_orders_feed()
        assert page.check_orders_in_order_feed(orders_history, orders_feed)

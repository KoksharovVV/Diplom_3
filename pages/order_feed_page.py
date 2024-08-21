import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.step("Нажать Лента Заказов")
    def click_on_order_in_order_feed(self):
        return self.find_element(locator=OrderFeedPageLocators.ORDER_IN_ORDER_FEED).click()

    @allure.step("Найти окно заказа")
    def find_order_window(self):
        return self.find_element(locator=OrderFeedPageLocators.WINDOW_ID_ORDER)

    @allure.step("Получить id заказов в ленте заказов")
    def get_orders_from_orders_feed(self):
        elements = self.find_elements(OrderFeedPageLocators.ORDER_FEED)
        orders_feed = [element.text for element in elements]
        return orders_feed

    @allure.step("Проверить, что все заказы из истории заказов отображаются в ленте заказов")
    def check_orders_in_order_feed(self, list1, list2):
        return all(value in list2 for value in list1)

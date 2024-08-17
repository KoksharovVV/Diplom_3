from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def click_on_order_in_order_feed(self):
        return self.find_element(locator=OrderFeedPageLocators.ORDER_IN_ORDER_FEED).click()

    def find_order_window(self):
        return self.find_element(locator=OrderFeedPageLocators.WINDOW_ID_ORDER)

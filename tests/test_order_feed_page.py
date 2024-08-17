from data import TestDataUrl
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:
    def test_open_window_with_order_details(self, driver):
        page = OrderFeedPage(driver)
        page.open_page(TestDataUrl.ORDER_FEED_URL)
        page.click_on_order_in_order_feed()
        assert page.find_order_window()

from data import TestDataUrl
from pages.main_page import MainPage


class TestMainPage:
    def test_click_on_constructor(self, driver):
        page = MainPage(driver)
        page.open_page(TestDataUrl.LOGIN_PAGE_URL)
        page.click_on_constructor()
        assert page.find_text_assemble_the_burger()

    def test_click_on_order_feed(self, driver):
        page = MainPage(driver)
        page.open_page(TestDataUrl.LOGIN_PAGE_URL)
        page.click_on_order_feed()
        assert page.find_text_order_feed()

    def test_open_window_with_details(self, driver):
        page = MainPage(driver)
        page.open_page(TestDataUrl.MAIN_URL)
        page.find_and_click_on_bun()
        assert page.find_text_ingredient_details()

    def test_close_window_with_details(self, driver):
        page = MainPage(driver)
        page.open_page(TestDataUrl.MAIN_URL)
        page.find_and_click_on_bun()
        page.find_and_click_close_ingredient_details()
        assert page.not_find_text_order_feed()

    def test_counter_ingredient(self, driver):
        page = MainPage(driver)
        page.open_page(TestDataUrl.MAIN_URL)
        page.drag_on_drop_item_to_order()
        assert page.save_text_counter() == "2"

    def test_create_order(self, driver, log_in):
        page = MainPage(driver)
        page.drag_on_drop_item_to_order()
        page.click_on_process_order_button()
        assert page.the_order_id_modal_windows_appears()

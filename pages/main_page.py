from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.personal_cabinet_pege_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def click_on_constructor(self):
        self.wait_and_click(locator=MainPageLocators.CONSTRUCTOR_BUTTON)

    def find_text_assemble_the_burger(self):
        return self.find_element(locator=MainPageLocators.ASSEMBLE_THE_BURGER_TEXT)

    def click_on_order_feed(self):
        self.wait_and_click(locator=MainPageLocators.ORDER_FEED_BUTTON)

    def find_text_order_feed(self):
        return self.find_element(locator=MainPageLocators.ORDER_FEED_BUTTON)

    def find_and_click_on_bun(self):
        self.wait_for_clickable(MainPageLocators.INGREDIENT_BUN).click()

    def find_text_ingredient_details(self):
        return self.wait_for_visibility(locator=MainPageLocators.INGREDIENT_DETAILS)

    def not_find_text_order_feed(self):
        return self.not_find_element(locator=MainPageLocators.INGREDIENT_DETAILS)

    def find_and_click_close_ingredient_details(self):
        return self.wait_for_clickable(locator=MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON).click()

    def drag_on_drop_item_to_order(self):
        element = self.find_element(locator=MainPageLocators.INGREDIENT_BUN)
        location = self.find_element(locator=MainPageLocators.ORDER_AREA)
        self.drag_and_drop_element(element_to_drag=element, target_location=location)

    def save_text_counter(self):
        return self.find_element(locator=MainPageLocators.BUN_INGREDIENT_COUNTER).text

    def click_on_process_order_button(self):
        self.wait_and_click(locator=MainPageLocators.MAKE_ORDER_BUTTON)

    def the_order_id_modal_windows_appears(self):
        return self.find_element(locator=MainPageLocators.WINDOW_ID_ORDER)

    def get_counter_completed_today(self):
        return self.find_element(locator=OrderFeedPageLocators.COUNTER_COMPLETED_TODAY).text

    def close_order_window(self):
        return self.wait_and_click(locator=OrderFeedPageLocators.CLOSE_ORDER_WINDOW)

    def get_counter_completed_for_all_time(self):
        return self.find_element(locator=OrderFeedPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME).text

    def disappearance_fake_id_in_order_window(self):
        self.disappeared_text(
            locator=MainPageLocators.ID_ORDER_IN_MODAL_WINDOW, text="9999")

    def get_id_order(self):
        return self.find_element(locator=MainPageLocators.ID_ORDER_IN_MODAL_WINDOW).text

    def create_order(self):
        self.drag_on_drop_item_to_order()
        self.click_on_process_order_button()
        self.disappearance_fake_id_in_order_window()
        order = self.get_id_order()
        self.close_order_window()
        return order

    def get_order_in_work(self):
        return self.wait_for_visibility(locator=OrderFeedPageLocators.ORDER_IN_WORK).text

    def open_personal_cabinet(self):
        self.find_element(MainPageLocators.PERSONAL_CABINET_BUTTON, 30).click()

    def open_history_orders(self):
        self.wait_and_click(locator=PersonalCabinetPageLocators.HISTORY_ORDERS_BUTTON)

    def get_id_orders_from_history(self):
        elements = self.find_elements(PersonalCabinetPageLocators.HISTORY_ORDERS)
        orders_history = [element.text for element in elements]
        return orders_history

    def get_orders_from_orders_feed(self):
        elements = self.find_elements(OrderFeedPageLocators.ORDER_FEED)
        orders_feed = [element.text for element in elements]
        return orders_feed

    @staticmethod
    def check_orders_in_order_feed(list1, list2):
        return all(value in list2 for value in list1)

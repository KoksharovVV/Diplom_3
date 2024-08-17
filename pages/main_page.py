from locators.main_page_locators import MainPageLocators
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

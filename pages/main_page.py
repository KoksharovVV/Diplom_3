import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Нажать 'Конструктор'")
    def click_on_constructor(self):
        self.wait_and_click(locator=MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Найти 'Собрать бургер'")
    def find_text_assemble_the_burger(self):
        return self.find_element(locator=MainPageLocators.ASSEMBLE_THE_BURGER_TEXT)

    @allure.step("Нажать 'Лента Заказов'")
    def click_on_order_feed(self):
        self.wait_and_click(locator=MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Найти 'Лента Заказов'")
    def find_text_order_feed(self):
        return self.find_element(locator=MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Найти и нажать на булочку")
    def find_and_click_on_bun(self):
        self.wait_for_clickable(MainPageLocators.INGREDIENT_BUN).click()

    @allure.step("Найти текст 'Детали ингредиента'")
    def find_text_ingredient_details(self):
        return self.wait_for_visibility(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Найти отсутствие текста 'Детали ингредиента'")
    def not_find_text_ingredient_details(self):
        return self.not_find_element(locator=MainPageLocators.INGREDIENT_DETAILS)

    @allure.step("Закрыть модалку 'Детали ингредиента'")
    def find_and_click_close_ingredient_details(self):
        return self.wait_for_clickable(locator=MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON).click()

    @allure.step("Перетащить ингредиент в заказ")
    def drag_on_drop_item_to_order(self):
        element = self.find_element(locator=MainPageLocators.INGREDIENT_BUN)
        location = self.find_element(locator=MainPageLocators.ORDER_AREA)
        self.drag_and_drop_element(element_to_drag=element, target_location=location)

    @allure.step("Получить число из счетчика ингредиента")
    def get_text_counter(self):
        return self.find_element(locator=MainPageLocators.BUN_INGREDIENT_COUNTER).text

    @allure.step("Нажать 'Оформить заказ'")
    def click_on_process_order_button(self):
        self.wait_and_click(locator=MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Найти модалку с заказом")
    def the_order_id_modal_windows_appears(self):
        return self.find_element(locator=MainPageLocators.WINDOW_ID_ORDER)

    @allure.step("Изменение id заказа в модалке заказа")
    def disappearance_fake_id_in_order_window(self):
        self.disappeared_text(
            locator=MainPageLocators.ID_ORDER_IN_MODAL_WINDOW, text="9999")

    @allure.step("Получить id заказа")
    def get_id_order(self):
        return self.find_element(locator=MainPageLocators.ID_ORDER_IN_MODAL_WINDOW).text

    @allure.step("Закрыть модалку заказа")
    def close_order_window(self):
        return self.wait_and_click(locator=MainPageLocators.CLOSE_ORDER_WINDOW)

    @allure.step("Создать заказ")
    def create_order(self):
        self.drag_on_drop_item_to_order()
        self.click_on_process_order_button()
        self.disappearance_fake_id_in_order_window()
        order = self.get_id_order()
        self.close_order_window()
        return order

    @allure.step("Открыть личный кабинет")
    def open_personal_cabinet(self):
        self.find_element(MainPageLocators.PERSONAL_CABINET_BUTTON, 30).click()

    @allure.step("Открыть личный кабинет")
    def open_personal_account(self):
        self.wait_for_clickable(MainPageLocators.PERSONAL_CABINET_BUTTON).click()

    @allure.step('Проверить исчезновение кнопки "Войти в аккаунт" при переходе в личный кабинет')
    def check_transition_on_personal_cabinet(self):
        return self.not_find_element(locator=MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Получить число из счетчика Выполненно сегодня")
    def get_counter_completed_today(self):
        return self.find_element(locator=MainPageLocators.COUNTER_COMPLETED_TODAY).text

    @allure.step("Получить число из счетчика Выполненно за все время")
    def get_counter_completed_for_all_time(self):
        return self.find_element(locator=MainPageLocators.COUNTER_COMPLETED_FOR_ALL_TIME).text

    @allure.step("Получить первый в списке заказ в работе")
    def get_order_in_work(self):
        return self.wait_for_visibility(locator=MainPageLocators.ORDER_IN_WORK).text

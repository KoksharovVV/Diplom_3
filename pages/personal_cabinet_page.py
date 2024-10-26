import allure
from pages.base_page import BasePage
from locators.personal_cabinet_pege_locators import PersonalCabinetPageLocators


class PersonalCabinetPage(BasePage):
    @allure.step("Открыть историю заказов")
    def click_history_orders(self):
        self.wait_for_clickable(PersonalCabinetPageLocators.HISTORY_ORDERS_BUTTON).click()

    @allure.step("Найти заголовок 'Профиль'")
    def find_label_profile(self):
        return self.find_element(locator=PersonalCabinetPageLocators.LABEL_PROFILE)

    @allure.step("Найти активную кнопку история заказов")
    def find_active_button_history_orders(self):
        return self.find_element(locator=PersonalCabinetPageLocators.HISTORY_OF_ORDERS_TEXT_ACTIVE)

    @allure.step("Нажать Выход")
    def click_exit(self):
        return self.find_element(locator=PersonalCabinetPageLocators.EXIT_BUTTON).click()

    @allure.step("Открыть историю заказов")
    def open_history_orders(self):
        self.wait_and_click(locator=PersonalCabinetPageLocators.HISTORY_ORDERS_BUTTON)

    @allure.step("Проверить отсутствие заголовка Профиль")
    def not_find_label_profile(self):
        return self.not_find_element(locator=PersonalCabinetPageLocators.LABEL_PROFILE)

    @allure.step("Получить id заказов из истории")
    def get_id_orders_from_history(self):
        elements = self.find_elements(PersonalCabinetPageLocators.HISTORY_ORDERS)
        orders_history = [element.text for element in elements]
        return orders_history

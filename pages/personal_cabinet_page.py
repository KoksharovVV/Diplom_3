import allure
from locators.login_page_locators import LoginPageLocators
from locators.personal_cabinet_pege_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage


class PersonalCabinetPage(BasePage):
    @allure.step("Открыть личный кабинет")
    def open_personal_account(self):
        self.wait_for_clickable(LoginPageLocators.PERSONAL_CABINET_BUTTON).click()

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

    @allure.step("Найти email инпут")
    def find_email_input(self):
        return self.find_element(locator=LoginPageLocators.LOGIN_LABEL)

from locators.login_page_locators import LoginPageLocators
from locators.personal_cabinet_pege_locators import PersonalCabinetPageLocators
from pages.base_page import BasePage


class PersonalCabinetPage(BasePage):
    def click_on_personal_account(self):
        self.wait_for_clickable(LoginPageLocators.PERSONAL_CABINET_BUTTON).click()

    def click_history_orders(self):
        self.wait_for_clickable(PersonalCabinetPageLocators.HISTORY_ORDERS_BUTTON).click()

    def find_label_profile(self):
        return self.find_element(locator=PersonalCabinetPageLocators.LABEL_PROFILE)

    def find_active_button_history_orders(self):
        return self.find_element(locator=PersonalCabinetPageLocators.HISTORY_OF_ORDERS_TEXT_ACTIVE)

    def click_exit(self):
        return self.find_element(locator=PersonalCabinetPageLocators.EXIT_BUTTON).click()

    def find_email_input(self):
        return self.find_element(locator=LoginPageLocators.LOGIN_LABEL)

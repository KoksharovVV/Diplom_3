import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from data import TestForgotData


class ForgotPasswordPage(BasePage):

    @allure.step("Найти заголовок 'Восстановить пароль'")
    def find_label_restore_password(self):
        return self.find_element(locator=ForgotPasswordPageLocators.LABEL_RESTORE_PASSWORD)

    @allure.step("Заполнить поле email")
    def set_email_input(self, email):
        email_input = self.wait_for_clickable(locator=ForgotPasswordPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    @allure.step("Нажать 'Восстановить'")
    def click_restore_button(self):
        self.wait_for_clickable(locator=ForgotPasswordPageLocators.BUTTON_RESTORE).click()

    @allure.step("Найти кнопку 'Сохранить'")
    def find_save_button(self):
        return self.find_element(locator=ForgotPasswordPageLocators.BUTTON_SAVE)

    @allure.step("Заполнить поле 'Пароль'")
    def set_password_input(self):
        password_input = self.wait_for_clickable(locator=ForgotPasswordPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestForgotData.password)

    @allure.step("Нажать на иконку глаза ")
    def click_on_eye(self):
        self.find_element(locator=ForgotPasswordPageLocators.EYE_ICON).click()

    @allure.step("Найти поле 'Пароль' после ")
    def find_field_active_field_password(self):
        return self.find_element(locator=ForgotPasswordPageLocators.ACTIVE_PASSWORD_INPUT)

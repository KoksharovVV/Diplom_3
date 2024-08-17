from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from data import TestForgotData


class ForgotPasswordPage(BasePage):
    def find_label_restore_password(self):
        return self.find_element(locator=ForgotPasswordPageLocators.LABEL_RESTORE_PASSWORD)

    def set_email_input_and_press_restore(self, email):
        email_input = self.wait_for_clickable(locator=ForgotPasswordPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    def click_restore_button(self):
        self.wait_for_clickable(locator=ForgotPasswordPageLocators.BUTTON_RESTORE).click()

    def find_save_button(self):
        return self.find_element(locator=ForgotPasswordPageLocators.BUTTON_SAVE)

    def set_password_input(self):
        password_input = self.wait_for_clickable(locator=ForgotPasswordPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestForgotData.password)

    def click_on_eye(self):
        self.find_element(locator=ForgotPasswordPageLocators.EYE_ICON).click()

    def find_field_active_field_password(self):
        return self.find_element(locator=ForgotPasswordPageLocators.ACTIVE_PASSWORD_INPUT)

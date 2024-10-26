import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import TestDataUrl, TestLoginPageData


class LoginPage(BasePage):

    @allure.step("Авторизация")
    def login(self):
        self.open_page(TestDataUrl.LOGIN_PAGE_URL)
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(TestLoginPageData.email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(TestLoginPageData.password)
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step("Найти email инпут")
    def find_email_input(self):
        return self.find_element(locator=LoginPageLocators.LOGIN_LABEL)

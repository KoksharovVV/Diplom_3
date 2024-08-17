from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import TestDataUrl, TestLoginPageData


class LoginPage(BasePage):
    def login(self):
        self.open_page(TestDataUrl.LOGIN_PAGE_URL)
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(TestLoginPageData.email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(TestLoginPageData.password)
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

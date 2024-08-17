from data import TestDataUrl, TestLoginPageData
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


class TestPasswordRecovery:
    def test_open_forgot_password_page(self, driver):
        page = LoginPage(driver)
        page.open_page(TestDataUrl.LOGIN_PAGE_URL)
        page.click_button_restore_password()
        assert page.find_label_restore_password()

    def test_enter_mail_and_click_restore_button_go_to_restore_page(self, driver):
        page = ForgotPasswordPage(driver)
        page.open_page(TestDataUrl.FORGOT_PASSWORD_PAGE_URL)
        page.set_email_input_and_press_restore(TestLoginPageData.email)
        page.click_restore_button()
        assert page.find_save_button()

    def test_click_on_the_eye_makes_field_active(self, driver):
        page = ForgotPasswordPage(driver)
        page.open_page(TestDataUrl.FORGOT_PASSWORD_PAGE_URL)
        page.set_email_input_and_press_restore(TestLoginPageData.email)
        page.click_restore_button()
        page.set_password_input()
        page.click_on_eye()
        assert page.find_field_active_field_password

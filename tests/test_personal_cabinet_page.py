from pages.personal_cabinet_page import PersonalCabinetPage


class TestPersonalCabinet:
    def test_click_personal_account(self, driver, log_in):
        page = PersonalCabinetPage(driver)
        page.click_on_personal_account()
        assert page.find_label_profile()

    def test_open_order_history(self, driver, log_in):
        login_page = PersonalCabinetPage(driver)
        login_page.click_on_personal_account()
        login_page.click_history_orders()
        assert login_page.find_active_button_history_orders()

    def test_exit_of_account(self, driver, log_in):
        login_page = PersonalCabinetPage(driver)
        login_page.click_on_personal_account()
        login_page.click_exit()
        assert login_page.find_email_input()

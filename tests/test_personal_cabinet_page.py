import allure
from pages.personal_cabinet_page import PersonalCabinetPage


class TestPersonalCabinet:
    @allure.title('Проверка перехода в личный кабинет')
    def test_click_personal_account(self, driver, log_in):
        page = PersonalCabinetPage(driver)
        page.open_personal_account()
        assert page.find_label_profile()

    @allure.title('Проверка перехода в ленту заказов')
    def test_open_order_history(self, driver, log_in):
        page = PersonalCabinetPage(driver)
        page.open_personal_account()
        page.click_history_orders()
        assert page.find_active_button_history_orders()

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_of_account(self, driver, log_in):
        page = PersonalCabinetPage(driver)
        page.open_personal_account()
        page.click_exit()
        assert page.find_email_input()

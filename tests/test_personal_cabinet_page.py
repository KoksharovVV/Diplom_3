import allure
from pages.personal_cabinet_page import PersonalCabinetPage
from pages.main_page import MainPage


class TestPersonalCabinet:
    @allure.title('Проверка перехода в личный кабинет')
    def test_click_personal_account(self, driver, log_in):
        page = MainPage(driver)
        page.open_personal_account()
        assert page.check_transition_on_personal_cabinet()

    @allure.title('Проверка перехода в ленту заказов')
    def test_open_order_history(self, driver, personal_account):
        page = PersonalCabinetPage(driver)
        page.click_history_orders()
        assert page.find_active_button_history_orders()

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_of_account(self, driver, personal_account):
        page = PersonalCabinetPage(driver)
        page.click_exit()
        assert page.not_find_label_profile()

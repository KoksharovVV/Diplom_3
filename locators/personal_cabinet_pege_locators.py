from selenium.webdriver.common.by import By


class PersonalCabinetPageLocators:
    LABEL_PROFILE = (By.XPATH, "//a[text()='Профиль']")  # Заголовок "Профиль"
    HISTORY_ORDERS_BUTTON = (
        By.XPATH, "//a[text()='История заказов']")  # Кнопка "История заказов"
    HISTORY_OF_ORDERS_TEXT_ACTIVE = (
        By.XPATH,
        "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='История заказов']")  # Активная кнопка "История заказов"
    EXIT_BUTTON = (By.XPATH, ".//button[@type='button' and text()='Выход']")
    HISTORY_ORDERS = (
        By.XPATH, ".//p[@class='text text_type_digits-default']")  # все заказы пользователя в разделе 'История заказов'

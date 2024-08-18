from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    LABEL_RESTORE_PASSWORD = (By.XPATH, ".//*[text()='Восстановление пароля']")  # Заголовок "Восстановление пароля"
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text']")  # Поле 'Email'
    BUTTON_RESTORE = (By.XPATH, ".//button[text()='Восстановить']")  # Кнопка "Восстановить"
    BUTTON_SAVE = (By.XPATH, ".//*[text()='Сохранить']")  # Кнопка "Сохранить"
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")  # Поле 'Пароль'
    EYE_ICON = (By.XPATH, ".//div[@class='input__icon input__icon-action']")  # Иконка просмотра/скрытия пароля
    ACTIVE_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_status_active')]")  # Акртивноый инпут пароль

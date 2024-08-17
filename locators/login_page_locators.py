from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text']")  # Поле 'Email'
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")  # Поле 'Пароль'
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка 'Войти'
    BUTTON_FORGOT_PASSWORD = (By.XPATH, ".//*[text()='Восстановить пароль']")  # Кнопка "Восстановить пароль"

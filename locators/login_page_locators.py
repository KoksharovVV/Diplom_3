from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text']")  # Поле 'Email'
    PASSWORD_INPUT = (By.XPATH, ".//input[@type='password']")  # Поле 'Пароль'
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # Кнопка 'Войти'
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в шапке страницы
    LOGIN_LABEL = (By.XPATH, ".//*[text()='Вход']")  # Заголовок "Вход"'

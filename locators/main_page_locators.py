from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в шапке страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка Конструктор
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")  # Кнопка Лента заказов
    ASSEMBLE_THE_BURGER_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Текст 'Соберите бургер'
    ORDER_FEED_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")  # Текст 'Лента заказов'
    INGREDIENT_BUN = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")  # Булка
    INGREDIENT_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")  # Текст 'Детали ингредиента'
    INGREDIENT_DETAILS_CLOSE_BUTTON = (
        By.XPATH, "(.//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    # Закрыть всплывающее окно 'Детали ингредиента'
    ORDER_AREA = (By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']")  # Список заказа на странице
    BUN_INGREDIENT_COUNTER = (
        By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p[starts-with(@class,'counter')]")
    # Счетчик ингредиента булка
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка 'Оформить заказ'
    WINDOW_ID_ORDER = (
        By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")  # Модальное окно 'Идентификатор заказа'

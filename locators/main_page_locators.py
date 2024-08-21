from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_LOGIN_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    PERSONAL_CABINET_BUTTON = (By.XPATH, ".//a[@href='/account']")  # Личный кабинет в шапке страницы
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка Конструктор
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")  # Кнопка Лента заказов
    ASSEMBLE_THE_BURGER_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Текст 'Соберите бургер'
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
    ID_ORDER_IN_MODAL_WINDOW = (By.XPATH,
                                ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    # номер заказа в модальном окне 'Идентификатор заказа'
    CLOSE_ORDER_WINDOW = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    # крестик для закрытия модального окна 'Идентификатор заказа'
    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]")
    # счетчик 'Выполнено за сегодня'
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]")
    # счетчик за все время 'Ленте Заказов'
    ORDER_IN_WORK = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
    # id заказа в статусе 'В работе'

from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_IN_ORDER_FEED = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
    # Заказ из списка заказов в 'Ленте заказов'
    WINDOW_ID_ORDER = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")  # Модалка 'Идентификатор заказа'
    COUNTER_COMPLETED_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p[1]")
    # счетчик 'Выполнено за сегодня'
    CLOSE_ORDER_WINDOW = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    # крестик для закрытия модального окна 'Идентификатор заказа'
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p[1]")
    # счетчик за все время 'Ленте Заказов'
    ORDER_IN_WORK = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
    # id заказа в статусе 'В работе'
    ORDER_FEED = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    # все заказы пользователя в разделе 'Лента заказов'

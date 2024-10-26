from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_IN_ORDER_FEED = (By.XPATH, "//li[@class='OrderHistory_listItem__2x95r mb-6']")
    # Заказ из списка заказов в 'Ленте заказов'
    WINDOW_ID_ORDER = (By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']")  # Модалка 'Идентификатор заказа'
    ORDER_FEED = (By.XPATH, ".//p[@class='text text_type_digits-default']")
    # все заказы пользователя в разделе 'Лента заказов'

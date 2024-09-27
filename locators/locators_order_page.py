from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_FIRST = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]') # Первый заказ в истории заказазов
    WINDOW_INFORMATION_ABOUT_ORDER = (By.XPATH, './/div[contains(@class, "Modal_orderBox__1xWdi")]/parent::div/parent::section') # Окно с информацией о заказе
    EMAIL_AUTHORIZATION = (By.XPATH,".//input[@class = 'text input__textfield text_type_main-default' and  @name = 'name']")  # Поле ввода email
    PASSWORD_AUTHORIZATION = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    BUTTON_ENTER = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти"
    INGREDIENT_FIRST = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]") # Первый ингредиент по списку
    BOX_FOR_INGREDIENTS = (By.XPATH, ".//div[@class = 'constructor-element constructor-element_pos_top']") # "Корзина" для ингридиентов
    BUTTON_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']") # Кнопка "Оформить заказ"
    BUTTON_CLOSE = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Кнопка закрытия окна
    ORDER_FIRST_OF_ORDER_LIST = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]') # Первый заказ в ленте заказов
    ORDER_NUMBER_IN_WINDOW = (By.XPATH, './/p[contains(@class, "text text_type_digits-default mb-10 mt-5")]') # Номер первого заказа в ленте заказов в открытом всплывающем окне
    ORDER_NUMBER_FROM_INFORMATION_WINDOW = (By.XPATH, './/h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]') # Номер заказа во всплывающем окне после оформления заказа
    COUNTER_ALL_ORDERS = (By.XPATH, '(.//p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"])[1]') # Счетчик всех заказов
    COUNTER_DAY_ORDERS = (By.XPATH, '(.//p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"])[2]') # Счетчик заказов за день
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, '(.//li[@class = "text text_type_digits-default mb-2"])[6]') # Номер заказа "В работе"
    ORDER_LAST_IN_ORDERS_HISTORY = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[last()]') # Последний заказ в истории заказов пользователя
    ORDER_NUMBER_OF_LAST_IN_ORDERS_HISTORY = (By.XPATH, '(.//p[@class = "text text_type_digits-default"])[last()]') # Номер последнего заказа в истории заказов пользователя
    ORDER_NUMBER_OF_FIRST_IN_ORDER_LIST = (By.XPATH, '(.//p[@class = "text text_type_digits-default"])[1]') # Номер самого верхнего заказа в листе заказов
    ORDER_ID = (By.XPATH, "//h2[text()='9999']") # Исчезающий номер заказа во всплывающем окне после оформления заказа
    MODAL_OVERLAY = [By.XPATH, '//*[contains(@class, "Modal_modal__loading")]/following::div[@class="Modal_modal_overlay__x2ZCr"]']
from selenium.webdriver.common.by import By


class AccountPageLocators:
    EMAIL_AUTHORIZATION = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and  @name = 'name']")  # Поле ввода email
    PASSWORD_AUTHORIZATION = (By.XPATH, ".//input[@name = 'Пароль']")  # Поле ввода пароля
    BUTTON_ENTER = (By.XPATH, ".//button[text() = 'Войти']")  # Кнопка "Войти"
    HEADER_CREATE_BURGER = (By.XPATH, ".//h1[text() = 'Соберите бургер']") #Кнопка "Собери бургер"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка "Личный кабинет"
    BUTTON_PROFILE = (By.XPATH, ".//a[text() = 'Профиль']") # Кнопка "Профиль"
    BUTTON_ORDERS_HISTORY = (By.XPATH, ".//a[text() = 'История заказов']") # Кнопка "История заказов"
    BUTTON_EXIT = (By.XPATH, ".//button[text() = 'Выход']") # Кнопка "Выход"
    BUTTON_ORDER = (By.XPATH, ".//button[text() = 'Оформить заказ']") # Кнопка "Оформить заказ"
    INFORMATION_ABOUT_ORDER = (By.XPATH, ".//p[text() = 'Ваш заказ начали готовить']") # Статус заказа
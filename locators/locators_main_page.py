from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_CONSTRUCTOR = (By.XPATH, '//li[1]//p') # Кнопка "Конструктор"
    BUTTON_ORDERS_LIST = (By.XPATH, './/li[2]//p') # Кнопка "Лента Заказов"
    INGREDIENT_FIRST = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient_')])[1]") # Первый ингредиент по списку
    HEADER_INGREDIENT_DETAILS = (By.XPATH, ".//h2[text() = 'Детали ингредиента']") # Заголовок Детали ингредиента
    BUTTON_CLOSE = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Кнопка закрытия окна
    BOX_FOR_INGREDIENTS = (By.XPATH, ".//div[@class = 'constructor-element constructor-element_pos_top']") # "Корзина" для ингридиентов
    INGREDIENT_COUNT = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[1]") # Счетчик ингредиентов
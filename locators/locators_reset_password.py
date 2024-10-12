

from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default']") # Поле ввода email
    BUTTON_RESET = (By.XPATH, './/button[text() = "Восстановить"]') # Кнопка "Восстановить"
    CODE_INPUT = (By.XPATH, './/label[text() = "Введите код из письма"]') # Поле ввода кода
    PASSWORD_INPUT = (By.XPATH, './/input[@type = "password"]') # Поле ввода
    ICON_EYE = (By.XPATH, './/div[@class = "input__icon input__icon-action"]') # Иконка глазик
    ICON_EYE_SHOW_PASSWORD = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']") # Иконка глазик пароль видно
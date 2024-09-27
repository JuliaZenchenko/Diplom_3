from selenium.webdriver.common.by import By


class LoginPageLocators:
    BUTTON_RESET_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]') #Кнопка Восстановить пароль
    HEADER_RESET_PASSWORD = (By.XPATH, './/h2[text()="Восстановление пароля"]') # Заголовок "Восстановление пароля"
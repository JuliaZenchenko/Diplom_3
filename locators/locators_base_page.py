from selenium.webdriver.common.by import By

class BasePageLocators:
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]') #Кнопка Личный кабинет
    NEW_PASSWORD_HEADER = (By.XPATH, './/h2[text()="Восстановление пароля"]') # Кнопка "Восстановление пароля" на странице авторизации
    WELCOME_BUTTON = (By.XPATH, './/button[text()="Войти"]') # Кнопка "Войти" на странице авторизации
import allure
import data

from pages.base_page import BasePage
from locators.locators_reset_password import ForgotPasswordLocators


class PageResetPassword(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу Восстановление пароля")
    def go_to_forgot_password_page(self):
        self.driver.get(data.MAIN_URL+data.FORGOT_PASSWORD_URL)

    @allure.step("Ввод email на странице Восстановление пароля")
    def email_input(self):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_INPUT, data.EMAIL)

    @allure.step("Ввод нового пароля на странице Восстановление пароля")
    def new_password_input(self):
        self.set_text_to_element(ForgotPasswordLocators.PASSWORD_INPUT, data.NEW_PASSWORD)

    @allure.step("Нажатие на кнопку 'Восстановить'")
    def click_on_button_reset(self):
        self.click_on_element(ForgotPasswordLocators.BUTTON_RESET)

    @allure.step("Ожидание появления поля Введите код из письма")
    def wait_code_input(self):
        self.wait_and_find_element(ForgotPasswordLocators.CODE_INPUT)

    @allure.step("Клик по иконке с глазиком")
    def click_on_icon_eye(self):
        self.click_on_element(ForgotPasswordLocators.ICON_EYE)

    @allure.step("Поиск иконки глазика когда виден пароль")
    def find_active_eye(self):
        return self.wait_and_find_element(ForgotPasswordLocators.ICON_EYE_SHOW_PASSWORD)

import data
import allure

from pages.base_page import BasePage
from locators.locators_main_page import MainPageLocators
from locators.locators_account_page import AccountPageLocators


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Авторизация на сайте под данными тестового пользователя")
    def authorization(self):
        self.driver.get(data.MAIN_URL + data.LOGIN_URL)
        self.set_text_to_element(AccountPageLocators.EMAIL_AUTHORIZATION, data.EMAIL)
        self.set_text_to_element(AccountPageLocators.PASSWORD_AUTHORIZATION, data.PASSWORD)
        self.click_on_element(AccountPageLocators.BUTTON_ENTER)
        self.wait_and_find_element(AccountPageLocators.HEADER_CREATE_BURGER)
        self.click_on_element(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.find_elements(AccountPageLocators.BUTTON_PROFILE)

    @allure.step("Клик по кнопке 'История заказов' в профиле авторизованного пользователя")
    def click_on_orders_history(self):
        self.click_on_element(AccountPageLocators.BUTTON_ORDERS_HISTORY)

    @allure.step("Клик по кнопке 'Выйти' в профиле авторизованного пользователя")
    def click_on_button_exit(self):
        self.click_on_element(AccountPageLocators.BUTTON_EXIT)

    @allure.step("Ожидание появления кнопки 'Войти' на странице авторизации")
    def wait_of_button_enter(self):
        self.wait_and_find_element(AccountPageLocators.BUTTON_ENTER)

    @allure.step("Создание заказа под авторизованным пользователем")
    def create_order(self):
        self.driver.get(data.MAIN_URL + data.LOGIN_URL)
        self.set_text_to_element(AccountPageLocators.EMAIL_AUTHORIZATION, data.EMAIL)
        self.set_text_to_element(AccountPageLocators.PASSWORD_AUTHORIZATION, data.PASSWORD)
        self.click_on_element(AccountPageLocators.BUTTON_ENTER)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FIRST, MainPageLocators.BOX_FOR_INGREDIENTS)

    @allure.step("Клик по кнопке 'Сделать заказ'")
    def click_on_button_order(self):
        self.click_on_element(AccountPageLocators.BUTTON_ORDER)

    @allure.step("Ожидание статуса заказа во всплывающем окне после оформления заказа")
    def wait_information_about_order(self):
        return self.wait_and_find_element(AccountPageLocators.INFORMATION_ABOUT_ORDER)
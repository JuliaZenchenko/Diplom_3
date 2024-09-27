from pages.base_page import BasePage
import data
from locators.locators_order_page import OrderPageLocators
from locators.locators_account_page import AccountPageLocators
from locators.locators_main_page import MainPageLocators
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по заказу")
    def click_on_order(self):
        self.click_on_element(OrderPageLocators.ORDER_FIRST)

    @allure.step("Поиск окна с информацией о заказе")
    def find_order_information_window(self):
        return self.wait_and_find_element(OrderPageLocators.WINDOW_INFORMATION_ABOUT_ORDER)

    @allure.step("Переход на страницу листа заказов")
    def go_to_order_page(self):
        self.driver.get(data.MAIN_URL+data.ORDER_URL)

    @allure.step("Ожидание статуса заказа во всплывающем окне после создания заказа")
    def wait_for_order_information(self):
        return self.wait_and_find_element(AccountPageLocators.INFORMATION_ABOUT_ORDER)

    @allure.step("Создание заказа")
    def create_order(self):
        self.driver.get(data.MAIN_URL+data.LOGIN_URL)
        self.set_text_to_element(OrderPageLocators.EMAIL_AUTHORIZATION, data.EMAIL)
        self.set_text_to_element(OrderPageLocators.PASSWORD_AUTHORIZATION, data.PASSWORD)
        self.click_on_element(OrderPageLocators.BUTTON_ENTER)
        self.drag_and_drop_element(OrderPageLocators.INGREDIENT_FIRST, OrderPageLocators.BOX_FOR_INGREDIENTS)
        self.click_on_element(OrderPageLocators.BUTTON_ORDER)
        self.wait_for_order_information()


    @allure.step("Получение номера заказа из истории заказов пользователя")
    def search_number_of_order(self):
        self.wait_until_clickable(OrderPageLocators.BUTTON_CLOSE)
        self.wait_invisibility(OrderPageLocators.MODAL_OVERLAY)
        self.wait_and_find_element(OrderPageLocators.BUTTON_CLOSE)
        self.click_on_element(OrderPageLocators.BUTTON_CLOSE)
        self.wait_until_clickable(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.click_on_element(AccountPageLocators.BUTTON_PERSONAL_ACCOUNT)
        self.wait_and_find_element(AccountPageLocators.BUTTON_PROFILE)
        self.click_on_element(AccountPageLocators.BUTTON_ORDERS_HISTORY)
        self.wait_and_find_element(OrderPageLocators.ORDER_FIRST)
        self.scroll_to_element(OrderPageLocators.ORDER_NUMBER_OF_LAST_IN_ORDERS_HISTORY)
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_OF_LAST_IN_ORDERS_HISTORY)

    @allure.step("Получение id заказа")
    def return_order_id(self):
        self.wait_until_missing_element(OrderPageLocators.ORDER_ID)
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_FROM_INFORMATION_WINDOW)

    @allure.step("Получение номера из последнего заказа в листе заказов")
    def number_of_last_order_in_order_list_from_order_history(self):
        self.go_to_order_page()
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_LIST)
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_OF_FIRST_IN_ORDER_LIST)

    @allure.step("Получение номера заказа из окна информации о заказе")
    def number_of_last_user_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_FROM_INFORMATION_WINDOW)

    @allure.step("Получение количества всех выполненных заказов")
    def get_count_of_all_orders(self):
        return self.get_text_from_element(OrderPageLocators.COUNTER_ALL_ORDERS)

    @allure.step("Получение количества всех заказов за день")
    def get_count_of_day_orders(self):
        return self.get_text_from_element(OrderPageLocators.COUNTER_DAY_ORDERS)

    @allure.step("Получение номера заказа в работе")
    def get_order_number_in_progress(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_NUMBER_IN_PROGRESS)
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_IN_PROGRESS)
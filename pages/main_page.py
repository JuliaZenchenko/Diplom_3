import allure
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.locators_main_page import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_button(self):
        self.click_on_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step("Клик по кнопке 'Лист заказов'")
    def click_on_button_orders_list(self):
        self.click_on_element(MainPageLocators.BUTTON_ORDERS_LIST)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_FIRST)

    @allure.step("Открытие всплывающего окна с деталями об ингредиенте")
    def open_window_ingredient_details(self):
        return self.wait_and_find_element(MainPageLocators.HEADER_INGREDIENT_DETAILS)

    @allure.step("Клик по крестику закрытия всплывающего окна")
    def click_on_button_close(self):
        self.click_on_element(MainPageLocators.BUTTON_CLOSE)

    @allure.step("Проверка, что всплывающее окно с информацией об ингредиенте закрыто")
    def check_window_close(self):
        return self.element_exist(MainPageLocators.HEADER_INGREDIENT_DETAILS)

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_FIRST, MainPageLocators.BOX_FOR_INGREDIENTS)

    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.wait_and_find_element(source_locator)
        target_element = self.wait_and_find_element(target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element)
        action.perform()

    @allure.step("Получение значения со счетчика ингредиента")
    def get_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNT)
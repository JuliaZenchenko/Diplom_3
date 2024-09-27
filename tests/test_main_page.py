

import data
import allure

from pages.main_page import MainPage

class TestMainPage:
    @allure.title("Проверка перехода по клику на Конструктор")
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_the_button_pers_account()
        main_page.click_on_constructor_button()
        main_url = main_page.get_current_url
        assert main_url == data.MAIN_URL

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_click_on_button_orders_list(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_button_orders_list()
        feed_url = main_page.get_current_url
        assert '/feed' in feed_url

    @allure.title("Проверка клика на ингредиент и появление всплывающего окна с деталями")
    def test_click_on_ingredient_and_open_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.open_window_ingredient_details()

    @allure.title("Проверка закрытия всплывающего окна кликом по крестику")
    def test_click_on_ingredient_and_check_window_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_on_button_close()
        assert main_page.check_window_close() is False

    @allure.title("Проверка, что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()

        assert main_page.get_ingredient_counter() == '2'
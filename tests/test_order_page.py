import allure

from pages.page_order import OrderPage


class TestOrderPage:
    @allure.title("Проверка, что если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_window_with_information_about_order(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.click_on_order()
        assert order_page.find_order_information_window()

    @allure.title(
        "Проверка, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_orders_are_displayed_in_order_list(self, driver):
        order_page = OrderPage(driver)
        order_page.create_order()
        number_of_user_order = order_page.search_number_of_order()
        number_in_number_list = order_page.number_of_last_order_in_order_list_from_order_history()
        assert number_of_user_order == number_in_number_list

    @allure.title("Проверка, что при создании нового заказа счётчик Выполнено за всё время увеличивается,")
    def test_count_of_all_orders(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        before_order = order_page.get_count_of_all_orders()
        order_page.create_order()
        order_page.number_of_last_user_order()
        order_page.go_to_order_page()
        after_order = order_page.get_count_of_all_orders()
        assert int(after_order) > int(before_order)

    @allure.title("Проверка, что при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_count_of_day_orders(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        before_order = order_page.get_count_of_day_orders()
        order_page.create_order()
        order_page.go_to_order_page()
        after_order = order_page.get_count_of_day_orders()
        assert int(after_order) > int(before_order)

    @allure.title("Проверка, что после оформления заказа его номер появляется в разделе В работе")
    def test_count_now_order(self, driver):
        order_page = OrderPage(driver)
        order_page.create_order()
        order_number = order_page.return_order_id()
        order_page.go_to_order_page()
        order_number_in_order_list = order_page.get_order_number_in_progress()
        assert order_number in order_number_in_order_list

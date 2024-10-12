import allure

from pages.page_account import AccountPage


class TestAccountPage:
    @allure.title("Проверка перехода в разел 'История заказов'")
    def test_click_on_history_of_orders(self, driver):
        account_page = AccountPage(driver)
        account_page.authorization()
        account_page.click_on_orders_history()
        order_history_url = account_page.get_current_url
        assert '/order-history' in order_history_url

    @allure.title("Проверка выхода из аккаунта")
    def test_click_on_exit(self, driver):
        account_page = AccountPage(driver)
        account_page.authorization()
        account_page.click_on_button_exit()
        account_page.wait_of_button_enter()
        login_url = account_page.get_current_url
        assert '/login' in login_url

    @allure.title("Проверка, что залогиненный пользователь может оформить заказ")
    def test_create_order_for_login_user(self, driver):
        account_page = AccountPage(driver)
        account_page.create_order()
        account_page.click_on_button_order()
        assert account_page.wait_information_about_order()
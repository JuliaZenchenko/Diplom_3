import allure

from pages.page_login import LoginPage


class TestLoginPage:
    @allure.title("Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_on_new_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.click_on_button_reset_password()
        forgot_password_url = login_page.get_current_url
        assert 'forgot-password' in forgot_password_url

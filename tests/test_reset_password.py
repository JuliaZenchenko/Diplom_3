import allure

from pages.page_reset_password import PageResetPassword


class TestForgotPasswordPage:
    @allure.title("Проверка перехода на страницу восстановления пароля кнопке Восстановить пароль")
    def test_send_email_for_reset(self, driver):
        forgot_password_page = PageResetPassword(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.email_input()
        forgot_password_page.click_on_button_reset()
        forgot_password_page.wait_code_input()
        reset_url = forgot_password_page.get_current_url
        assert '/reset-password' in reset_url

    @allure.title("Проверка того, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_password_show(self, driver):
        forgot_password_page = PageResetPassword(driver)
        forgot_password_page.go_to_forgot_password_page()
        forgot_password_page.email_input()
        forgot_password_page.click_on_button_reset()
        forgot_password_page.wait_code_input()
        forgot_password_page.new_password_input()
        forgot_password_page.click_on_icon_eye()
        assert forgot_password_page.find_active_eye()
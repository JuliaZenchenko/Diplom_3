import allure

from pages.base_page import BasePage


class TestBasePage:
    @allure.title("Проверка клика по кнопке 'Личный кабинет'")
    def test_click_on_cabinet_button(self, driver):
        base_page = BasePage(driver)
        base_page.click_on_the_button_pers_account()
        login_url = base_page.get_current_url
        assert '/login' in login_url

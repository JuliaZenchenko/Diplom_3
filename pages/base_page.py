import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_base_page import BasePageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from faker import Faker


class BasePage:

    def __init__(self, driver):
        self.driver=driver

    @allure.step("Поиск элемента с задержкой")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидание пока элемент станет кликабельным")
    def wait_until_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        filter_field = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return filter_field.click()

    @allure.step("Ожидание, пока элемент станет невидимым на странице")
    def wait_invisibility(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не исчез за {timeout} секунд.")
    @allure.step("Поиск элемента")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Получение текста из элемента")
    def get_text_from_element(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text

    @allure.step("Добавление текста в элемент")
    def set_text_to_element(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


    @property
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_the_button_pers_account(self):
        self.click_on_element(BasePageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step("Проверка поиска элемента с ожиданием")
    def element_exist(self, locator):
        try:
            self.driver.wait_and_find_element(locator)
            return True
        finally:
            return False

    @allure.step("Зажать элемент и перенести на нужное место")
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.wait_and_find_element(source_locator)
        target_element = self.wait_and_find_element(target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element)
        action.perform()

    @allure.step("Ожидание исчезновения элемента")
    def wait_until_missing_element(self, locator, time=10):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(locator))

    @allure.step('Генерация почты пароля имени для юзера')
    def generate_create():
        fake = Faker()
        email = fake.email(domain="yandex.ru")
        password = fake.password()

        return email, password


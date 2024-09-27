import allure
import pytest
import data

from selenium import webdriver

@pytest.fixture(scope='function', params=['chrome', 'firefox'])
@allure.title('Запуск драйвера')
def driver(request):
    driver = None
    
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    driver.get(data.MAIN_URL)

    yield driver

    driver.quit()


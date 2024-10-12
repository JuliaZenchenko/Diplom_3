# Diplom_3

DIPLOM_3 
Цель: составить автоматизированные тесты для проверки сервиса заказа бургеров:https://stellarburgers.nomoreparties.site/

1. Написание тестов произведено в PyCharm  с подключенными модулями Selenium, Pytest, Allure
2. Автотесты написаны в соответствии с POM
3. Команда для запуска тестов — pytest 
4. Команда для запуска с записью отчета в allure_results: pytest --alluredir=allure_results

Директория проекта:
* allure_results - директория с отчетами allure
* locators - директория локаторов
* pages - директория методов страниц
* tests - директория тестов
* conftest.py - фикстуры
* data.py - вспомогательные данные(URL и данные тестового юзера)
* README.md - описание проекта
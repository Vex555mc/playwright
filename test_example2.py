# Тимошенко Павел Тимурович
# Дата: 2026.11.12
# Время: 14:50
# Описание: пример из playwright
# код открывает главную страницу playwright.dev и проверяет её адрес
# я скопировал пример и запущу его локально
# изменение: вынес адрес сайта и перевёл
# сообщения на русский и добавил проверку заголовка

import pytest
from playwright.sync_api import Page, expect
import re

# изменено: адрес вынесен и строка не дублируется
BASE_URL = "https://playwright.dev/"


@pytest.fixture(scope="function", autouse=True) #изменил autoselect на autouse чтобы не было ошибки
def before_each_after_each(page: Page):
    print("before the test runs")  #сообщение до перехода на страницу

    #переход на стартовую страницу перед тестом
    page.goto(BASE_URL)

    yield  #тест выполняется

    print("after the test runs")  #сообщение после завершения теста


def test_main_navigation(page: Page):
    #изменено: адрес сравнивается с BASE_URL
    expect(page).to_have_url(BASE_URL)

    #добавлено: проверка, что в заголовке есть слово playwright
    expect(page).to_have_title(re.compile(r"Playwright$"))

#day1: пример из paywright, добавлена проверка заголовка и вынесен BASE_URL

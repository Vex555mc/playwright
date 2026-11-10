# Тимошенко Павел Тимурович
# Дата: 2026-11-10
# Время: 15:06

# 1) проверка что есть нужное слово через test_has_title 
# 2) проверка заголовка после перехода по ссылке (test_get_started_link) и поиск элементов через get_by_role, ссылку и заголовок link и heading соответственно

import re
from playwright.sync_api import Page, expect

# открывает страницу по ссылке и проверяет слово
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # проверяем заголовок вкладки
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # нажатие на кнопку
    page.get_by_role("link", name="Get started").click()

    # проверяем что нужный заголовок виден на странице
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# day1: скопирован и запущен первый пример из документации Playwright


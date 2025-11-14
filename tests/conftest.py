import os
import pytest
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
# Загружаем переменные из .env файла
load_dotenv()

# Фикстура для логина - выполняется перед каждым тестом
@pytest.fixture
def logged_in_page(page: Page):
    """Фикстура которая логинится и возвращает страницу"""
    # Получаем данные из .env файла
    base_url = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    username = os.getenv("SAUCE_USER", "standard_user")
    password = os.getenv("SAUCE_PASS", "secret_sauce")

    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()

    # Проверяем что логин успешен
    expect(page.locator(".inventory_list")).to_be_visible()

    return page


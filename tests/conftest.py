import os
import pytest
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
# Загружаем переменные из .env файла
load_dotenv()
from datetime import datetime

# Фикстура для логина - выполняется перед каждым тестом
@pytest.fixture
def logged_in_page(page: Page):
    """Фикстура которая логинится и возвращает страницу"""
    # Получаем данные из .env файла
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SAUCE_USER")
    password = os.getenv("SAUCE_PASS")

    page.goto(base_url)
    page.locator("[data-test=\"username\"]").fill(username)
    page.locator("[data-test=\"password\"]").fill(password)
    page.locator("[data-test=\"login-button\"]").click()

    # Проверяем что логин успешен
    expect(page.locator(".inventory_list")).to_be_visible()

    return page

@pytest.fixture
def screenshot_on_failure(page, request):
    """Делает скриншот при падении теста"""
    yield
    if request.node.rep_call.failed:
        # Создаем папку для скриншотов если её нет
        os.makedirs("screenshots", exist_ok=True)
        # Генерируем уникальное имя файла
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        test_name = request.node.name
        screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
        page.screenshot(path=screenshot_path)
        print(f"Скриншот сохранен: {screenshot_path}")
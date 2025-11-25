import os
import pytest
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
from datetime import datetime

# Получаем абсолютный путь к директории, где находится conftest.py
# Получаем абсолютный путь к директории, где находится conftest.py
current_dir = os.path.dirname(os.path.abspath(__file__)) #__file__ - говорит: "Где я нахожусь?",abspath - превращает это в полный адрес,dirname - берет только папку, где лежит файл
env_path = os.path.join(current_dir, '.env.standard') #Собирает полный путь к файлу с настройками Как сказать: "В той же папке, где я нахожусь, найди файл '.env.standard'"

print(f"Абсолютный путь к .env.standard: {env_path}")
print(f"Файл существует: {os.path.exists(env_path)}")

# Загружаем переменные из .env.standard файла
load_dotenv(env_path)

# Проверяем загрузку
print("=== Проверка загруженных переменных ===")
print(f"BASE_URL: '{os.getenv('BASE_URL')}'")
print(f"SAUCE_USER: '{os.getenv('SAUCE_USER')}'")
print(f"SAUCE_PASS: '{os.getenv('SAUCE_PASS')}'")


# Фикстура для логина - выполняется перед каждым тестом
@pytest.fixture
def logged_in_page(page: Page):
    """Фикстура которая логинится и возвращает страницу"""
    # Получаем данные из .env.standard файла
    base_url = os.getenv("BASE_URL")
    username = os.getenv("SAUCE_USER")
    password = os.getenv("SAUCE_PASS")

    print(f"В фикстуре - BASE_URL: {base_url}")
    print(f"В фикстуре - SAUCE_USER: {username}")
    print(f"В фикстуре - SAUCE_PASS: {password}")

    if not base_url:
        raise ValueError("BASE_URL не загружен! Проверьте файл .env.standard")

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

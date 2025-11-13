import pytest
import os
from dotenv import load_dotenv

# Явно укажите путь к вашему файлу
load_dotenv('.env.standart')

from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def open_saucedemo(page: Page):
    page.goto(
        "https://www.saucedemo.com/",
        timeout=60000,  # 60 секунд вместо 30
        wait_until="domcontentloaded"  # Ждем только DOM, а не полную загрузку
    )
    return page

# @pytest.fixture()
# def login_credentials(page: Page):
#     """Фикстура возвращает логин и пароль из .env"""
#     load_dotenv('.env.standart', override=True)  # override=True перезаписывает системные, борьба с подтягивание имя юзера с компа
#     return {
#         "username":
#         os.getenv("SAUCE_USER","none"),
#         "password":
#         os.getenv("SAUCE_PASS","none")
#     }
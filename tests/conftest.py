import pytest
import os

from playwright.sync_api import Page, expect

@pytest.fixture(autouse=True)
def open_saucedemo(page: Page):
    page.goto(
        "https://www.saucedemo.com/",
        timeout=60000,  # 60 секунд вместо 30
        wait_until="domcontentloaded"  # Ждем только DOM, а не полную загрузку
    )
    return page

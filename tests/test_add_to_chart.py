import re

import pytest
from playwright.sync_api import Page, expect


def test_log_in_standard_user(page: Page):
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()
    # Ждем загрузки следующей страницы
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url(re.compile("https://www.saucedemo.com/inventory.html"))

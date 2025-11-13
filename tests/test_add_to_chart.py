import re

import pytest
from playwright.sync_api import Page, expect
# def test_open_login_page(page: Page):
#     expect(page).to_have_title(re.compile("Swag Labs"))
#     print("The password entry page contains the words Swag Labs")
#
# def test_login_link(page: Page):
#     expect(page.locator('[data-test="login-button"]')).to_be_enabled()
#     print("button login link enable")

def test_log_in_standard_user(page: Page):
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_text("Login").click()
    # Ждем загрузки следующей страницы
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page).to_have_url(re.compile("https://www.saucedemo.com/inventory.html"))


# def test_log_in_standard_user(page: Page,login_credentials):
#     page.get_by_placeholder("Username").fill(login_credentials["username"])
#     page.get_by_placeholder("Password").fill(login_credentials["password"])
#     page.get_by_text("Login").click()
#     # Ждем загрузки следующей страницы
#     page.wait_for_url("https://www.saucedemo.com/inventory.html")
#     expect(page).to_have_url(re.compile("https://www.saucedemo.com/inventory.html"))
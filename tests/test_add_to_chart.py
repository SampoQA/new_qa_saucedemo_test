import pytest
from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")  #go to site
    expect(page).to_have_title("Swag Labs")



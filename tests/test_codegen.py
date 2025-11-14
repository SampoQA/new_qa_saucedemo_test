import os
import pytest
from playwright.sync_api import Page, expect
from dotenv import load_dotenv
# Загружаем переменные из .env файла
load_dotenv()

def test_add_items_to_cart(logged_in_page):
    """Тест добавления товаров в корзину"""
    page = logged_in_page

    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"item-1-title-link\"]").click()
    page.locator("[data-test=\"add-to-cart\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()

    # Проверяем что корзина видима (значит товары добавились)
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()


def test_remove_item_from_cart(logged_in_page):
    """Тест удаления товара из корзины"""
    page = logged_in_page

    # Сначала добавляем товар
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"item-2-title-link\"]").click()

    # Потом удаляем
    page.locator("[data-test=\"remove\"]").click()

    # Переходим в корзину и проверяем
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"checkout\"]")).to_contain_text("Checkout")


def test_complete_purchase(logged_in_page):
    """Тест полного процесса покупки"""
    page = logged_in_page

    # Добавляем товар
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    # Переходим к оформлению
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"checkout\"]").click()

    # Заполняем информацию
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    page.locator("[data-test=\"firstName\"]").fill("Test")
    page.locator("[data-test=\"lastName\"]").fill("Test")
    page.locator("[data-test=\"postalCode\"]").fill("123456")

    # Продолжаем
    page.locator("[data-test=\"continue\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Overview")

    # Завершаем заказ
    page.locator("[data-test=\"finish\"]").click()
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Complete!")
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")
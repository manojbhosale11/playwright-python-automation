
import pytest
from playwright.sync_api import Page, expect

from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.mark.smoke
@pytest.mark.cart
def test_added_product_appears_in_cart(
    logged_in_page: Page,
):
    products = ProductsPage(logged_in_page)
    cart = CartPage(logged_in_page)
    product_name = "Sauce Labs Backpack"

    products.add_to_cart(product_name)
    products.open_cart()

    expect(cart.page_title).to_have_text("Your Cart")
    expect(cart.cart_items).to_have_count(1)
    expect(cart.cart_item_names).to_have_text([product_name])


@pytest.mark.cart
def test_multiple_products_appear_in_cart(
    logged_in_page: Page,
):
    products = ProductsPage(logged_in_page)
    cart = CartPage(logged_in_page)

    products.add_to_cart("Sauce Labs Backpack")
    products.add_to_cart("Sauce Labs Bike Light")
    products.open_cart()

    expect(cart.cart_items).to_have_count(2)
    expect(
        cart.cart_item("Sauce Labs Backpack")
    ).to_have_count(1)
    expect(
        cart.cart_item("Sauce Labs Bike Light")
    ).to_have_count(1)


@pytest.mark.cart
def test_remove_product_from_cart(logged_in_page: Page):
    products = ProductsPage(logged_in_page)
    cart = CartPage(logged_in_page)
    product_name = "Sauce Labs Backpack"

    products.add_to_cart(product_name)
    products.open_cart()
    cart.remove_item(product_name)

    expect(cart.cart_items).to_have_count(0)
    expect(products.cart_badge).to_be_hidden()


import pytest
from playwright.sync_api import Page, expect

from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.products
def test_products_are_displayed(logged_in_page: Page):
    products = ProductsPage(logged_in_page)

    expect(products.page_title).to_have_text("Products")
    expect(products.product_items).to_have_count(6)


@pytest.mark.products
def test_add_product_to_cart(logged_in_page: Page):
    products = ProductsPage(logged_in_page)
    product_name = "Sauce Labs Backpack"

    products.add_to_cart(product_name)

    # The button changes after adding the product.
    expect(
        products.product_card(product_name).get_by_role(
            "button", name="Remove"
        )
    ).to_be_visible()

    # The cart badge should show one item.
    expect(products.cart_badge).to_have_text("1")


@pytest.mark.products
def test_remove_product_from_listing(logged_in_page: Page):
    products = ProductsPage(logged_in_page)
    product_name = "Sauce Labs Backpack"

    products.add_to_cart(product_name)
    products.remove_from_products_page(product_name)

    expect(
        products.product_card(product_name).get_by_role(
            "button", name="Add to cart"
        )
    ).to_be_visible()

    expect(products.cart_badge).to_be_hidden()


@pytest.mark.sorting
def test_sort_products_by_price_low_to_high(logged_in_page: Page,):
    products = ProductsPage(logged_in_page)

    products.sort_by("lohi")

    price_texts = products.product_prices.all_text_contents()
    prices = [
        float(price.replace("$", "").strip())
        for price in price_texts
    ]

    assert prices == sorted(prices), (
        f"Products are not sorted by ascending price: {prices}"
    )

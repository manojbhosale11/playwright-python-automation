import re
import pytest
from playwright.sync_api import Page, expect
from settings import INVENTORY_URL
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def open_checkout(page: Page) -> CheckoutPage:
    """Add a product and navigate to customer information."""
    products = ProductsPage(page)
    products.add_to_cart("Sauce Labs Backpack")
    products.open_cart()

    cart = CartPage(page)
    cart.proceed_to_checkout()

    return CheckoutPage(page)


@pytest.mark.checkout
@pytest.mark.parametrize(
    ("first_name", "last_name", "postal_code", "expected_error"),
    [
        ("", "Bhosale", "400706", "First Name is required"),
        ("Manoj", "", "400706", "Last Name is required"),
        ("Manoj", "Bhosale", "", "Postal Code is required"),
    ],
    ids=[
        "missing-first-name",
        "missing-last-name",
        "missing-postal-code",
    ],
)
def test_checkout_customer_information_validation(
    logged_in_page: Page,
    first_name: str,
    last_name: str,
    postal_code: str,
    expected_error: str,
):
    checkout = open_checkout(logged_in_page)

    checkout.enter_customer_information(
        first_name, last_name, postal_code
    )
    checkout.continue_to_overview()

    expect(checkout.error_message).to_be_visible()
    expect(checkout.error_message).to_contain_text(expected_error)


@pytest.mark.checkout
def test_order_overview_and_price_calculation(
    logged_in_page: Page,
):
    checkout = open_checkout(logged_in_page)

    checkout.enter_customer_information(
        "Manoj", "Bhosale", "400706"
    )
    checkout.continue_to_overview()

    expect(checkout.page_title).to_have_text("Checkout: Overview")
    expect(checkout.overview_item_names).to_have_text(
        ["Sauce Labs Backpack"]
    )

    # Verify the displayed price for the selected product.
    expect(checkout.subtotal_label).to_contain_text("$29.99")

    # Extract numeric amounts from the summary labels.
    def amount_from(locator) -> float:
        text = locator.inner_text()
        match = re.search(r"\$([\d]+\.[\d]{2})", text)

        assert match is not None, (
            f"Could not extract a price from: {text}"
        )

        return float(match.group(1))

    subtotal = amount_from(checkout.subtotal_label)
    tax = amount_from(checkout.tax_label)
    total = amount_from(checkout.total_label)

    # Verify that the displayed total equals subtotal plus tax.
    assert round(subtotal + tax, 2) == total, (
        f"Incorrect order total: subtotal={subtotal}, "
        f"tax={tax}, total={total}"
    )


@pytest.mark.smoke
@pytest.mark.checkout
def test_complete_purchase_successfully(
    logged_in_page: Page,
):
    checkout = open_checkout(logged_in_page)

    checkout.enter_customer_information(
        "Manoj", "Bhosale", "400706"
    )
    checkout.continue_to_overview()

    expect(checkout.page_title).to_have_text("Checkout: Overview")
    expect(checkout.finish_button).to_be_visible()

    checkout.finish_order()

    expect(checkout.page_title).to_have_text("Checkout: Complete!")
    expect(checkout.complete_header).to_have_text(
        "Thank you for your order!"
    )

    # Verify that the cart is empty after completion.
    products = ProductsPage(logged_in_page)
    expect(products.cart_badge).to_be_hidden()

    checkout.return_to_products()
    expect(logged_in_page).to_have_url(
        INVENTORY_URL
    )

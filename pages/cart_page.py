
from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = page.locator(".title")
        self.cart_items = page.locator(".cart_item")
        self.cart_item_names = page.locator(
            ".cart_item .inventory_item_name"
        )
        self.checkout_button = page.locator("#checkout")

    def cart_item(self, product_name: str):
        """Find a specific product inside the cart."""
        return self.cart_items.filter(has_text=product_name)

    def remove_item(self, product_name: str):
        self.cart_item(product_name).get_by_role(
            "button", name="Remove"
        ).click()

    def proceed_to_checkout(self):
        self.checkout_button.click()

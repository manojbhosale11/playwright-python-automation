
from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.page_title = page.locator(".title")
        self.product_items = page.locator(".inventory_item")
        self.product_prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def product_card(self, product_name: str):
        """Find a product card by its name."""
        return self.product_items.filter(has_text=product_name)

    def add_to_cart(self, product_name: str):
        self.product_card(product_name).get_by_role(
            "button", name="Add to cart"
        ).click()

    def remove_from_products_page(self, product_name: str):
        self.product_card(product_name).get_by_role(
            "button", name="Remove"
        ).click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    def open_cart(self):
        self.cart_link.click()

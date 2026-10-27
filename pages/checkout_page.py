
from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        # Customer information form
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.error_message = page.locator('[data-test="error"]')

        # Order overview
        self.page_title = page.locator(".title")
        self.overview_item_names = page.locator(
            ".cart_item .inventory_item_name"
        )
        self.subtotal_label = page.locator(".summary_subtotal_label")
        self.tax_label = page.locator(".summary_tax_label")
        self.total_label = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")

        # Order completion
        self.complete_header = page.locator(".complete-header")
        self.back_to_products_button = page.locator(
            "#back-to-products"
        )

    def enter_customer_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_to_overview(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def return_to_products(self):
        self.back_to_products_button.click()

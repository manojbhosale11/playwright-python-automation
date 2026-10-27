from playwright.sync_api import Page, expect
from settings import BASE_URL


def test_saucedemo_login_page_loads(page: Page):
    page.goto(BASE_URL)

    expect(page).to_have_title("Swag Labs")
    expect(page.get_by_placeholder("Username")).to_be_visible()
    expect(page.get_by_placeholder("Password")).to_be_visible()

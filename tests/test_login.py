
import pytest
from playwright.sync_api import Page, expect
from settings import TEST_USERNAME, TEST_PASSWORD, INVENTORY_URL
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login(TEST_USERNAME, TEST_PASSWORD)

    expect(page).to_have_url(INVENTORY_URL)
    expect(page.get_by_text("Products", exact=True)).to_be_visible()


@pytest.mark.regression
def test_invalid_login(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login("invalid_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )


@pytest.mark.regression
def test_login_with_empty_username(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login("", "secret_sauce")

    expect(login_page.error_message).to_contain_text(
        "Username is required"
    )


@pytest.mark.regression
def test_login_with_empty_password(page: Page):
    login_page = LoginPage(page)
    login_page.open()

    login_page.login("standard_user", "")

    expect(login_page.error_message).to_contain_text(
        "Password is required"
    )

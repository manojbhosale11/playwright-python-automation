import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from settings import (
    TEST_USERNAME,
    TEST_PASSWORD,
    INVENTORY_URL,
)


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(TEST_USERNAME, TEST_PASSWORD)

    expect(page).to_have_url(INVENTORY_URL)

    return page
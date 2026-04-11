import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture(scope="function", autouse=True)
def goto(page: Page, base_url):
    """Fixture to navigate to the base URL."""
    page.goto(base_url)


@pytest.fixture
def login_with_admin(page: Page):
    LoginPage(page).login_with_valid_admin()

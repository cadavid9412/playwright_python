import pytest
from playwright.sync_api import sync_playwright
from pages.login import SiteLogin


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Login before test
        login_page = SiteLogin(page)
        login_page.loadPage()
        yield page
        browser.close()

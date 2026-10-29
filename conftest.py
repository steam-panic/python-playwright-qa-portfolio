import pytest
from playwright.sync_api import Page

@pytest.fixture
def homepage(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    return page
import json
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def test_data():
    with open("data/users.json") as f:
        return json.load(f)

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

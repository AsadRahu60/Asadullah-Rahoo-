import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_valid_login(page, test_data):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    assert inventory_page.is_loaded()

@pytest.mark.regression
def test_invalid_login(page, test_data):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(test_data["invalid_user"]["username"], test_data["invalid_user"]["password"])
    assert "error" in login_page.get_error_message().lower()

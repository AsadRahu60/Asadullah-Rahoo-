from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart(page, test_data):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.load()
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    assert page.is_visible(cart_page.checkout_button)

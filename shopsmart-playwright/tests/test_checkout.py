from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(page, test_data):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.load()
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_checkout_info("John", "Doe", "12345")
    checkout_page.finish_checkout()
    assert "THANK YOU" in checkout_page.get_success_message().upper()

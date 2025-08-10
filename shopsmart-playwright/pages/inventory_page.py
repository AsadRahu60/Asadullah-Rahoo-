from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = ".inventory_list"
        self.add_to_cart_button = "button[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_icon = ".shopping_cart_link"

    def is_loaded(self):
        return self.page.is_visible(self.inventory_container)

    def add_backpack_to_cart(self):
        self.page.click(self.add_to_cart_button)

    def go_to_cart(self):
        self.page.click(self.cart_icon)

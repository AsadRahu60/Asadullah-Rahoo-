from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = "input[data-test='firstName']"
        self.last_name = "input[data-test='lastName']"
        self.zip_code = "input[data-test='postalCode']"
        self.continue_btn = "input[data-test='continue']"
        self.finish_btn = "button[data-test='finish']"
        self.success_msg = ".complete-header"

    def fill_checkout_info(self, first, last, zip_code):
        self.page.fill(self.first_name, first)
        self.page.fill(self.last_name, last)
        self.page.fill(self.zip_code, zip_code)
        self.page.click(self.continue_btn)

    def finish_checkout(self):
        self.page.click(self.finish_btn)

    def get_success_message(self):
        return self.page.inner_text(self.success_msg)

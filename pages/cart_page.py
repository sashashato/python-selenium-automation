from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CartPage(Page):
    EMPTY_CART_MSG = (By. XPATH, "//*[contains(text(),'Your cart is empty')]")

    def verify_empty_cart_message(self):
        empty_text = self.find_element(*self.EMPTY_CART_MSG)
        assert "Your cart is empty" in empty_text.text, "Empty cart message not found"
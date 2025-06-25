from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class CartPage(Page):
    EMPTY_CART_MSG = (By. XPATH, "//*[contains(text(),'Your cart is empty')]")
    CART_ITEMS = (By.XPATH, "//div[@data-test='cart-container']")

    def open_cart_page(self):
        self.driver.get('https://www.target.com/cart')

    def verify_empty_cart_message(self):
        empty_text = self.find_element(*self.EMPTY_CART_MSG)
        assert "Your cart is empty" in empty_text.text, "Empty cart message not found"

    def verify_product_in_cart(self):
        cart_items = self.driver.find_elements(*self.CART_ITEMS)
        assert len(cart_items) > 0, "Cart is empty. Expected at least 1 item."
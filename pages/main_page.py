from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    FIRST_ADD_TO_CART_BTN = (By.XPATH, "//button[.='Add to cart']")
    SIDE_ADD_BTN = (By.XPATH, "//button[@data-test='orderPickupButton']")

    def open_main_page(self):
        self.driver.get('https://target.com')

    def add_first_product_to_cart(self):
        self.wait_for_element_click(*self.FIRST_ADD_TO_CART_BTN)

    def confirm_add_in_side_menu(self):
        self.wait_for_element(*self.SIDE_ADD_BTN)
        self.wait_for_element_click(*self.SIDE_ADD_BTN)
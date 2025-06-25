from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Header(Page):
    ACCOUNT_BTN = (By.ID, 'account-sign-in')
    SIGN_IN_SIDE_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")


    def click_account(self):
        self.wait_for_element_click(*self.ACCOUNT_BTN)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def click_sign_in_from_nav(self):
        self.wait_for_element_click(*self.SIGN_IN_SIDE_BTN)

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)
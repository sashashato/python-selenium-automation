from selenium.webdriver.common.by import By
from pages.base_page import Page

class LoginPage(Page):
    SIGN_IN_MESSAGE = (By.XPATH, "//*[contains(text(), 'Sign in or create account')]")
    TERMS_AND_COND_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions']")

    def open_login_page(self):
        self.driver.get('https://www.target.com/orders?lnk=acct_nav_my_account')

    def verify_sign_in_message(self):
        self.wait_for_element(*self.SIGN_IN_MESSAGE)
        actual_text = self.find_element(*self.SIGN_IN_MESSAGE).text
        assert "Sign in or create account" in actual_text, "Sign in message not found"

    def click_terms_and_conditions_link(self):
        self.click(*self.TERMS_AND_COND_LINK)

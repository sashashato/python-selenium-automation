from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from features.steps.header_steps import CART_ICON

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
EMPTY_CART_MSG = (By.XPATH, "//*[contains(text(),'Your cart is empty')]")

@given('I open target.com')
def open_main(context):
    context.app.main_page.open_main_page()

@when('I click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()
    # cart_icon = WebDriverWait(context.driver, 10).until (EC.element_to_be_clickable((By. CSS_SELECTOR, "[data-test='@web/CartIcon']")) ).click()


@then('I should see "Your cart is empty" message')
def verify_message(context):
    context.app.cart_page.verify_empty_cart_message()
    # context.driver.implicitly_wait(5)
    # empty_text = context.driver.find_element(By. XPATH, "//*[contains(text(),'Your cart is empty')]")
    # assert "Your cart is empty" in empty_text.text
    # context.driver.quit()
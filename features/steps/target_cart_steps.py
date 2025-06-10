from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open target.com')
def open_main(context):
    context.driver.get("https://target.com")

@when('I click on cart icon')
def click_cart_icon(context):
    context.cart_icon = context.driver.find_element(By. CSS_SELECTOR, "[data-test='@web/CartIcon']").click()

@then('I should see "Your cart is empty" message')
def verify_message(context):
    context.driver.implicitly_wait(5)
    empty_text = context.driver.find_element(By. XPATH, "//*[contains(text(),'Your cart is empty')]")
    assert "Your cart is empty" in empty_text.text
    context.driver.quit()
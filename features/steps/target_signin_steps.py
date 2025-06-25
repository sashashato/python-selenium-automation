from behave import when, then
from selenium import webdriver
# from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ACCOUNT_BTN = (By.ID, 'account-sign-in')
# SIGN_IN_SIDE_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
@when('I click on Account')
def click_account(context):
    context.app.header.click_account()

@when('I click on Sign in or create account from side navigation')
def click_sign_in_nav(context):
    context.app.header.click_sign_in_from_nav()

@then('I should see the "Sign in or create account" message')
def verify_sign_in_message(context):
    context.app.login_page.verify_sign_in_message()

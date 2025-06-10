from behave import when, then
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

@when('I click on Account')
def click_account(context):
    context.driver.implicitly_wait(5)
    account_button = context.driver.find_element (By. XPATH, "//a[@id='account-sign-in']")
    account_button.click()
    sleep(1)

@when('I click on Sign in or create account from side navigation')
def click_sign_in_nav(context):
    sign_in_link = context.driver.find_element(By. XPATH, "//button[@data-test='accountNav-signIn']")
    sign_in_link.click()
    sleep(2)

@then('I should see the "Enter your email or mobile number to continue" message')
def verify_sign_in_message(context):
    message = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Enter your email or mobile number to continue')]")
    assert "Enter your email or mobile number to continue" in message.text

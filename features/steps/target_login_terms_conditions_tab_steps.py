from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open login page')
def open_login_page(context):
    context.app.login_page.open_login_page()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.login_page.get_current_window_id()

@when('Click on Target terms and conditions link')
def click_terms_and_conditions_link(context):
    context.app.login_page.click_terms_and_conditions_link()

@when('Switch to the newly opened window')
def switch_window(context):
    context.app.login_page.switch_to_new_window()

@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_opened(context):
    context.app.terms_and_conditions_page.verify_terms_and_conditions_page_opened()


@then('User can close new window and switch back to original')
def close_page(context):
    context.app.base_page.close_window()

def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)

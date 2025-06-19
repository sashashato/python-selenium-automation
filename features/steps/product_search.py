from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located(SEARCH_INPUT))
    search.clear()
    search.send_keys(search_word)
    # sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    button = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable(SEARCH_SUBMIT)).click()
    # sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    WebDriverWait(context.driver, 10).until(EC.url_contains(search_word))
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected {search_word} in URL but got {context.driver.current_url}'

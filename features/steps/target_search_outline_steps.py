from behave import when, then
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@when ('I search for "{product}"')
def search_product(context, product):
    context.app.header.search_product(product)

@then ('I should see results related "{product}"')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)
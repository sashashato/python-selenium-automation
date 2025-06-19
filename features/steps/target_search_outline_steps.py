from behave import when, then
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when ('I search for "{product}"')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # sleep(5)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-test='lp-resultsCount']")))

@then ('I should see results related "{product}"')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"

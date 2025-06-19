from behave import given, when, then
from selenium.webdriver.common.by import By
# from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given ('I open Target Circle page')
def open_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    # sleep(5)
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-test='storycardWrapperElement']")) )

@then ('I should see at least 10 benefit blocks')
def verify_benefit_blocks(context):
    benefit_blocks = context.driver.find_elements(By.XPATH, "//div[@data-test='storycardWrapperElement']")
    count = len(benefit_blocks)
    assert count >= 10, f"Expected at least 10 benefit blocks, but found {count}"
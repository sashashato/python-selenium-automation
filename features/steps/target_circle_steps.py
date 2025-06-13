from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given ('I open Target Circle page')
def open_circle_page(context):
    context.driver.get("https://www.target.com/circle")
    sleep(5)

@then ('I should see at least 10 benefit blocks')
def verify_benefit_blocks(context):
    benefit_blocks = context.driver.find_elements(By.XPATH, "//div[@data-test='storycardWrapperElement']")
    count = len(benefit_blocks)
    assert count >= 10, f"Expected at least 10 benefit blocks, but found {count}"
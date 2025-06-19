from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "a[aria-label*='Color'")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

@given('Open the Target product page "{}"')
def open_page(context, url):
    context.driver.get(url)
    context.wait = WebDriverWait(context.driver, 10)

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black Wash', 'Brown', 'Medium Wash']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    print(colors)

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep

@when ('I add first product from homepage to cart')
def add_first_product(context):
    # add_buttons = WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[.='Add to cart']")) )
    # # add_buttons = context.driver.find_elements(By.XPATH, "//button[.='Add to cart']")
    # add_buttons.click()
    # WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-test='orderPickupButton']")) )
    # # sleep(3)
    context.app.main_page.add_first_product_to_cart()

@when ('I confirm adding product in the side menu')
def confirm_add_in_side_menu(context):
    # side_add_button = context.driver.find_element(By.XPATH, "//button[@data-test='orderPickupButton']")
    # side_add_button.click()
    # # sleep(3)
    context.app.main_page.confirm_add_in_side_menu()

@when ('I open the cart page')
def open_cart(context):
    # context.driver.get("https://www.target.com/cart")
    # # sleep(3)
    # WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-test='cart-container']")) )
    context.app.cart_page.open_cart_page()

@then ('I should see product in the cart')
def verify_product_in_cart(context):
    # sleep(3)
    # cart_items = context.driver.find_elements(By.XPATH, "//div[@data-test='cart-container']")
    # assert len(cart_items) > 0, "Cart is empty. Expected at least 1 item."
    context.app.cart_page.verify_product_in_cart()
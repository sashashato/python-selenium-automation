# # 1. Practice with locators.
# from selenium.webdriver.common.by import By
#
# class AmazonSignInPageLocators:
#     amazon_logo = (By .CSS_SELECTOR, '.a-icon.a-icon-logo')
#     email_field = (By .CSS_SELECTOR, '.a-input-text')
#     continue_button = (By .ID, "continue")
#     conditions_of_use_link = (By .LINK_TEXT, "Conditions of Use")
#     privacy_notice_link = (By .LINK_TEXT, "Privacy Notice")
#     need_help_link = (By .CSS_SELECTOR, '.a-list-item')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
time.sleep(5)

amazon_logo = driver.find_element(By .CSS_SELECTOR, '.a-icon.a-icon-logo')
assert amazon_logo.is_displayed(), "Amazon logo not found"
print("Amazon logo found")

email_field = driver.find_element(By .CSS_SELECTOR, '.a-input-text')
assert email_field.is_displayed(), "Email field not found"
print("Email field found")

continue_button = driver.find_element(By .ID, "continue")
assert continue_button.is_displayed(), "Continue button not found"
print("Continue button found")

conditions_of_use_link = driver.find_element(By .LINK_TEXT, "Conditions of Use")
assert conditions_of_use_link.is_displayed(), "Conditions of Use not found"
print("Conditions of Use found")

privacy_notice_link = driver.find_element(By .LINK_TEXT, "Privacy Notice")
assert privacy_notice_link.is_displayed(), "Privacy notice not found"
print("Privacy notice found")

need_help_link = driver.find_element(By .CSS_SELECTOR, '.a-list-item')
assert need_help_link.is_displayed(), "Need help link not found"
print("Need help link found")

print("Test passed: Amazon Sign-In page elements are verified successfully.")






# # 2. Create a test case for the SignIn page using python & selenium script.
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time
#
# chrome_options = Options()
# chrome_options.add_argument('--incognito')
#
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get('https://www.target.com/')
# time.sleep(3)
#
# account_button = driver.find_element(By .XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']")
# account_button.click()
# time.sleep(2)
#
# sign_in_buton = driver.find_element(By .XPATH, "//button[@data-test='accountNav-signIn']")
# sign_in_buton.click()
# time.sleep(3)
#
# header = driver.find_element(By .XPATH, "//h1[contains(text(), 'Sign in or create account')]")
# sign_in_submit_button = driver.find_element(By.ID, "login")
# print("Test passed: Sign In page opened successfully.")
#
# driver.quit()




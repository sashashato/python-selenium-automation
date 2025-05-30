# 1. Practice with locators.
# from selenium.webdriver.common.by import By
# class AmazonSignInPageLocators:
#     amazon_logo = (By .XPATH, "//i[@aria-label='Amazon']")
#     email_field = (By .ID, "ap_email_login")
#     continue_button = (By .ID, "continue")
#     conditions_of_use_link = (By .LINK_TEXT, "Conditions of Use")
#     privacy_notice_link = (By .LINK_TEXT, "Privacy Notice")
#     need_help_link = (By .XPATH, "//a[@class='a-size-base a-link-normal']")





# 2. Create a test case for the SignIn page using python & selenium script.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument('--incognito')

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.target.com/')
time.sleep(3)

account_button = driver.find_element(By .XPATH, "//span[@class='sc-43f80224-3 fBDEOp h-margin-r-x3']")
account_button.click()
time.sleep(2)

sign_in_buton = driver.find_element(By .XPATH, "//button[@data-test='accountNav-signIn']")
sign_in_buton.click()
time.sleep(3)

header = driver.find_element(By .XPATH, "//h1[contains(text(), 'Sign in or create account')]")
sign_in_submit_button = driver.find_element(By.ID, "login")
print("Test passed: Sign In page opened successfully.")

driver.quit()




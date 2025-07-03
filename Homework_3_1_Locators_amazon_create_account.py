from selenium.webdriver.common.by import By
class AmazonCreateAccountPageLocators:

    amazon_logo = (By.CSS_SELECTOR, "a-icon.a-icon-logo")
    sign_in_or_create_account = (By.CSS_SELECTOR, ".a-size-medium-plus")
    enter_mobile_number_or_email_field = (By.ID, "ap_email_login")
    continue_button = (By.CSS_SELECTOR, "a-button-input")
    conditions_of_use_link = (By.CSS_SELECTOR, "[href*='ap_signin_notification_condition_of_use']")
    privacy_notice_link = (By.CSS_SELECTOR, "[href*='ap_signin_notification_privacy_notice']")
    need_help_link = (By.CSS_SELECTOR, ".a-size-base")
    create_a_free_business_account_link = (By.ID, "ab-registration-ingress-link")

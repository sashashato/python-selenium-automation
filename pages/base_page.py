from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def wait_for_element(self, *locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} still visible'
        )

    def wait_for_url_contains(self, partial_url):
        self.wait.until(EC.url_contains(partial_url), message=f'Expected {partial_url} not in URL')

    def get_current_window_id(self ):
        window = self.driver.current_window_handle
        print(f'Original window {window}')
        return window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        all_windows = self.driver.window_handles
        print(f'Switching to a new window: {all_windows[1]}')
        self.driver.switch_to.window(all_windows[1])

    def switch_to_window_by_id(self, window_id):
        print(f'Switching to a window: {window_id}')
        self.driver.switch_to.window(window_id)

    def close_window(self):
        self.driver.close()

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected '{expected_text}' but got '{actual_text}'"
from pages.base_page import Page

class MainPage(Page):
    def open_main_page(self):
        self.driver.get('https://target.com')

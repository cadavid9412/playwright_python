from playwright.sync_api import Page


class SiteLogin:
    def __init__(self, page: Page):
        self.page = page
        self.login_button = page.locator("text = SIGN UP OR LOGIN")
        self.login_option = page.get_by_role("button", name="OR LOGIN", exact=True)
        self.user_field = page.get_by_role("textbox", name="Email")
        self.password_field = page.get_by_role("textbox", name="Password")
        self.login = page.get_by_role("button", name="LOG IN")

    def loadPage(self):
        self.page.goto("https://www.theautomationchallenge.com/")
        self.login_button.click()
        self.login_option.click()
        self.user_field.click()
        self.user_field.fill("sebastian.cadavid9412@gmail.com")
        self.password_field.click()
        self.password_field.fill("python12345")
        self.login.click()

from playwright.sync_api import Page
import re


class formInput:
    def __init__(self, page: Page):
        self.page = page
        ##selectors input form process
        self.start = page.get_by_role("button", name="Start")
        self.sudmit = page.get_by_role("button", name="Submit")

    def fill_dynamic_field(self, label_text: str, value: str):
        container = self.page.locator("div").filter(
            has_text=re.compile(rf"^{re.escape(label_text)}$")
        )
        input_box = container.get_by_role("textbox").first
        input_box.fill(value)

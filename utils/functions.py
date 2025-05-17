import openpyxl
from playwright.sync_api import Page


def read_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data


def handle_recaptcha_if_present(page: Page):
    try:
        captcha = page.locator(
            "text=Get through this reCAPTCHA to continuepresentationPrivacyTerms"
        )

        if captcha.is_visible(timeout=1000):
            print("CAPTCHA detected — attempting to bypass or wait.")
            try:
                captcha.locator("img").click(timeout=2000)
            except:
                pass
            try:
                page.get_by_role("button", name="presentation").click(timeout=2000)
            except:
                pass
    except:
        pass

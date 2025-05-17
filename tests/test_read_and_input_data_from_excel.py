from pages.form import formInput
from utils.functions import read_excel_data, handle_recaptcha_if_present


def test_fill_form_with_excel_data(page):
    field_map = {
        "EIN": 0,
        "Company Name": 1,
        "Sector": 2,
        "Address": 3,
        "Automation Tool": 4,
        "Annual Saving": 5,
        "Date": 6,
    }
    excel_data = read_excel_data("./resources/challenge.xlsx")
    form_page = formInput(page)
    form_page.start.click()
    for row in excel_data:
        for label, index in field_map.items():
            handle_recaptcha_if_present(page)
            form_page.fill_dynamic_field(label, row[index])

        handle_recaptcha_if_present(page)
        form_page.sudmit.click()
        handle_recaptcha_if_present(page)

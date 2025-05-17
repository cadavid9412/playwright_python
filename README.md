# Playwright Automated Test with Python

This project show you how to run automated Playwright test in python that reads user data from excel file and fills a form, the project is structure with POM.

## Prerequisites

- python 3.11 or higher

## setup instructions

1. **clone repository**

```bash
git clone https://github.com/cadavid9412/playwright_python
```

2. **install dependencies and virtual environment**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
playwright install
```

3. **Run tests**
```bash
pytest .\tests\read_and_input_data_from_excel.py
```

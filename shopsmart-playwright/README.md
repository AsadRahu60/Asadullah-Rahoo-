# ShopSmart E2E – Playwright + PyTest + Allure

Automated UI testing of the [SauceDemo](https://www.saucedemo.com/) e-commerce site using Playwright with Python, PyTest, and Allure reporting.

## Features
- Page Object Model (POM) structure
- Smoke & regression test separation
- Data-driven login tests
- End-to-end checkout flow
- Allure HTML reports with screenshots

## Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
```

## Run Tests
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Example Test Types
- Smoke tests (`pytest -m smoke`)
- Regression tests (`pytest -m regression`)

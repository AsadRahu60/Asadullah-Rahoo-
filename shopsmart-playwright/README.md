# ShopSmart E2E – Playwright + PyTest + Allure

[![CI – Playwright](https://github.com/AsadRahu60/Asadullah-Rahoo-/actions/workflows/playwright.yml/badge.svg)](https://github.com/AsadRahu60/Asadullah-Rahoo-/actions/workflows/playwright.yml)

Automated UI testing of the [SauceDemo](https://www.saucedemo.com/) e-commerce site using **Playwright (Python)**, **PyTest**, and **Allure** reporting.  
**Kurz:** End-to-End Web-Tests (Login, Warenkorb, Checkout) mit moderner Testautomatisierung und Reportings.

---

## Features
- Page Object Model (POM) – clean, maintainable tests
- Smoke & regression markers (`@smoke`, `@regression`)
- Data-driven login tests (`data/users.json`)
- Full checkout flow (add to cart → checkout → success)
- Allure HTML reports with screenshots & traces on failure
- Ready for CI (GitHub Actions)

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

# RoboShop QA Suite – Robot Framework (UI + API)

Hybrid, keyword-driven test automation using Robot Framework that covers:
- UI tests against the OpenCart demo shop (https://demo.opencart.com/)
- API tests against Fake Store API (https://fakestoreapi.com/)
- A hybrid scenario demonstrating end-to-end thinking

## Features
- Robot Framework with SeleniumLibrary (UI) and RequestsLibrary (API)
- Tags for `smoke`, `ui`, `api`, `hybrid`
- Readable, reusable keywords in `resources/`
- HTML report (`report.html`) and log (`log.html`) generated after each run
- GitHub Actions CI uploads the report as an artifact

## Setup (macOS)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Ensure Google Chrome is installed
# Run tests headless by default via suite setup
```

## Run
```bash
# run all
robot --outputdir reports tests

# run only UI
robot --include ui --outputdir reports tests/ui_tests.robot

# run only API
robot --include api --outputdir reports tests/api_tests.robot

# run smoke
robot --include smoke --outputdir reports tests
```

## Recruiter Pitch (you can say this)
“I built a Robot Framework project that combines UI and API testing in a keyword-driven way. The UI part uses SeleniumLibrary to automate a public demo shop, while the API part validates endpoints from a public API. I separated reusable keywords and variables for maintainability and added tags to support smoke vs. full runs. The suite runs in GitHub Actions and publishes the Robot HTML report as a build artifact, mirroring how acceptance tests are run in CI.”

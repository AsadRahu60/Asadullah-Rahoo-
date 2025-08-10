# Selenide POM Shop Tests (Java + JUnit5 + Allure)

UI automation for the OpenCart demo using Java 17, Selenide (on top of Selenium), JUnit 5, and Allure reporting. Implements Page Object Model (POM) and runs in CI with headless Chrome.

## Features
- Java + Selenide + JUnit5 + Allure
- Page Object Model with `pages/`
- Smoke & regression tagging
- Allure results in `target/allure-results`
- GitHub Actions CI to run tests and upload Allure artifacts

## Recruiter Pitch
“I created a Java UI test framework using Selenide (on Selenium) and JUnit 5. I structured it with Page Objects for maintainability and used Allure for rich reports. A GitHub Actions workflow runs the tests in headless Chrome on each push and uploads Allure results so stakeholders can review the run artifacts.”

## Prerequisites
- Java 17
- Maven
- Google Chrome (local runs)

## Run locally
```bash
mvn -B -q test
# Allure results at: target/allure-results

# (optional) Generate HTML if you have Allure installed locally:
# allure generate target/allure-results --clean -o target/allure-report
# allure open target/allure-report
```

## Project Structure
```
src/main/java/pages/      # Page Objects
src/test/java/tests/      # JUnit tests
pom.xml
.github/workflows/ci.yml
```

## CI
- See `.github/workflows/ci.yml`
- Runs `mvn test` on Ubuntu with Chrome headless
- Uploads `target/allure-results` as artifact

# API Quality Checks – Postman + Newman + CI

Automated API testing suite for the Restful Booker API using Postman and Newman with an HTML report and GitHub Actions CI.

## What this shows
- Postman collection with full CRUD flow (auth, create, get, update, delete)
- Environment variables & dynamic data (token, bookingId)
- Newman CLI run with `htmlextra` HTML report
- CI pipeline that runs on every push and uploads the report as an artifact

## Quick start
```bash
# install deps
npm install

# run tests locally
npm run test

# open HTML report
open reports/report.html   # macOS
```

## Files
```
collections/booking_api.postman_collection.json
environments/booking_env.postman_environment.json
reports/   # HTML output after run
```

## CI (GitHub Actions)
See `.github/workflows/ci.yml`. The workflow:
- checks out code
- sets up Node.js
- installs newman + reporter
- runs the collection
- uploads `reports/report.html` as an artifact

## Recruiter Pitch (use this)
“I built an automated API testing project that validates the main flows of a booking API. I authored a Postman collection with JavaScript assertions for status codes, schema, and fields; used environment variables for dynamic values; ran the suite headlessly with Newman and generated an HTML report; and wired it into GitHub Actions so every push triggers a run and stores the report. This mimics how QA teams do API testing in CI/CD.”

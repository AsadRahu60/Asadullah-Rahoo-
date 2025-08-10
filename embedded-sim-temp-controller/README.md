# Embedded Simulation – Smart Temperature Controller

End-to-end embedded testing project that runs **without hardware** using PlatformIO (native), Unity (C unit tests), and Python (integration tests). CI builds the firmware, runs both test layers, and uploads an **Allure HTML report**.

## Diagram
```
          ┌──────────────────────────┐
          │  PyTest Integration Tests │
          │ (Allure reporting)        │
          └─────────────┬─────────────┘
                        │  stdin/stdout (simulated serial)
          ┌─────────────▼─────────────┐
          │  Native Firmware Program   │
          │  (PlatformIO, C/C++)       │
          └─────────────┬─────────────┘
                        │
            ┌───────────▼───────────┐
            │ Unity C Unit Tests     │
            │ (Firmware Logic)       │
            └────────────────────────┘
```

## What this shows
- Firmware logic in C with thresholds & state machine
- Unity unit tests for boundary/negative cases (ISTQB techniques)
- Python integration tests talk to the firmware via a simulated serial (process pipes)
- CI on GitHub Actions builds & tests everything and uploads Allure HTML

## Local run (macOS/Linux)
```bash
# Unit tests (C, Unity)
cd firmware
pip3 install platformio
pio test -e native

# Build the native firmware binary for integration tests
pio run -e native

# Integration tests (Python + Allure)
cd ../integration_tests
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pytest --alluredir ../reports/allure-pytest
```

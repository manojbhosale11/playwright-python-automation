
# Playwright Python Automation Framework

End-to-end automation testing framework built with
Python, Playwright and Pytest.

## Project Overview

This project automates key user journeys in the SauceDemo
e-commerce demo application.

The framework follows the Page Object Model (POM) design
pattern and uses reusable Pytest fixtures.

## Tech Stack

- Python
- Playwright
- Pytest
- pytest-playwright
- pytest-html
- python-dotenv
- Git and GitHub
- GitHub Actions

## Test Coverage

### Login
- Valid login
- Invalid credentials
- Required-field validation

### Products
- Product listing verification
- Add and remove products
- Price sorting

### Shopping Cart
- Verify cart contents
- Multiple products
- Remove products from cart

### Checkout
- Customer information validation
- Order overview
- Subtotal, tax and total validation
- Successful purchase flow

## Project Structure

pages/       - Page Object classes
tests/       - Automated test cases
conftest.py  - Shared test fixtures
settings.py  - Environment configuration
pytest.ini   - Pytest configuration
reports/     - HTML test report
test-results/ - Failure debugging artifacts

## Setup

Clone the repository, then enter its directory.

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

python -m pip install -r requirements.txt

Install the Chromium browser:

python -m playwright install chromium

## Run Tests

Run the complete test suite:

python -m pytest -v

Run the checkout tests:

python -m pytest -v tests/test_checkout.py

Run smoke tests:

python -m pytest -v -m smoke

Generate an HTML report:

python -m pytest -v \
  --html=reports/report.html \
  --self-contained-html

## Debugging

Screenshots, videos and traces are configured to be
retained on test failures.

Inspect saved artifacts in the test-results directory.

## Application Under Test

https://www.saucedemo.com/

This is a public demo application used for practice.

## Author

Manoj Bhosale

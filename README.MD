# Restful Booker API Tests 🏨

[![**Allure**](https://img.shields.io/badge/allure-2.27.0-yellow.svg?style=for-the-badge&logo=allure&logoColor=black)](https://github.com/allure-framework/allure2)
[![**Python**](https://img.shields.io/badge/python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![**Pytest**](https://img.shields.io/badge/pytest-8.3.5-green.svg?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![**Docker**](https://img.shields.io/badge/docker-24.0.5-blue.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![**GitHub Actions**](https://img.shields.io/badge/github--actions-automation-purple.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

---

## Overview

Automated API tests for the Restful Booker application using Python, Pytest, and Allure for reporting.  
Tests run inside Docker containers with CI/CD pipeline support via GitHub Actions.

---

## Project Structure 📁

RestfulBookerAPI/
├── tests/
│ ├── test_orders.py
│ ├── conftest.py
├── utils/
│ └── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── README.md
└── .github/
└── workflows/
└── api_tests.yml


---

## Features ✨

- 🧪 Pytest test framework for API validation  
- 📊 Allure reporting with HTML dashboard  
- 🐳 Dockerized test environment  
- 🔄 GitHub Actions CI pipeline with GitHub Pages report publishing  
- 🔐 Environment variables for flexible config  

---

## Prerequisites

- Docker & Docker Compose installed  
- Python 3.12+ (if running tests locally)  
- Git  

---

## Installation & Setup

```bash
git clone https://github.com/shlomi10/RestFullBookerBackend.git
cd restfulbooker-api-tests
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Configuration
Update environment variables in utils/.env (or use GitHub secrets):
```bash
BASE_URL=https://restful-booker.herokuapp.com
ADMIN_USER=admin
ADMIN_PW=password123
```

Running Tests 🚀
Run all tests locally:
```bash
pytest tests/ --alluredir=allure-results -v
```

Run with Docker Compose:
```bash
docker compose up --build
```

Run a specific test inside Docker:
```bash
docker compose run --rm api-tests pytest tests/test_orders.py::test_create_order
```
Viewing Allure Reports
Locally (via Docker Allure service):
http://localhost:5050/projects/default/reports/latest/index.html

Published on GitHub Pages (after CI run):
https://shlomi10.github.io/RestFullBookerBackend/

CI/CD Pipeline 🔄
GitHub Actions workflow automatically runs tests on push/pull requests to main, generates Allure reports, and publishes them to GitHub Pages.

Contributing 👥
Fork the repo

Create a new branch

Make your changes

Submit a pull request

Follow conventional commit messages

License
MIT License © 2025 Shlomi

Future Enhancements 🚀
Add negative test scenarios

Parallel test execution

API performance testing

Extended environment support

Integration with Slack for notifications

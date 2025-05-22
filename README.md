# Restfull Booker API Tests 🏨

[![Allure](https://img.shields.io/badge/Allure-2.27.0-yellow.svg?style=for-the-badge&logo=allure&logoColor=black)](https://github.com/allure-framework/allure2)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Test_Framework-green.svg?style=for-the-badge&logo=pytest)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-orange.svg?style=for-the-badge&logo=allure)](https://docs.qameta.io/allure/)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg?style=for-the-badge&logo=docker)](https://docs.docker.com/compose/)
[![CI Build](https://img.shields.io/github/actions/workflow/status/shlomi10/RestFullBookerBackend/api-tests.yml?label=CI%20Build&style=for-the-badge&logo=github-actions)](https://github.com/shlomi10/RestFullBookerBackend/actions/workflows/api-tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure%20Report-View%20Live-purple?style=for-the-badge&logo=github)](https://shlomi10.github.io/RestFullBookerBackend/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge&logo=license)](LICENSE)

---

## 🚀 Overview

Automated API testing framework for the **Restful Booker** application using **Python**, **Pytest**, **Docker**, and **Allure** reports.  
CI/CD integration via **GitHub Actions**, with automated report publishing to **GitHub Pages**.

---

## 📂 Project Structure

```
RestfullBookerBackend/
├── tests/
│   ├── test_bookings.py
│   ├── conftest.py
├── utils/
│   ├── .env
│   ├── api_client.py
│   ├── data_fixtures.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .github/
    └── workflows/
        └── api_tests.yml
```

---

## ✨ Features

- 🧪 Modular Pytest-based test suites
- 📊 Allure HTML test reports
- 🐳 Full Docker support for environment management
- 🔁 CI via GitHub Actions with automatic report publishing
- 🔐 Secure environment config using `.env` or GitHub Secrets

---

## ⚙️ Prerequisites

- Docker & Docker Compose
- Python 3.12+ (optional for local runs)
- Git

---

## 🛠 Installation & Setup

```bash
git clone https://github.com/shlomi10/RestFullBookerBackend.git
cd restfulbooker-api-tests
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔧 Configuration

Edit environment variables in `utils/.env`:

```env
BASE_URL=https://restful-booker.herokuapp.com
ADMIN_USER=admin
ADMIN_PW=password123
```

---

## ✅ Running Tests

Local:

```bash
pytest tests/ --alluredir=allure-results -v
```

Docker Compose:

```bash
docker compose up --build
```

Run specific test:

```bash
docker compose run --rm api-tests pytest tests/test_orders.py::test_create_order
```

---

## 📊 Viewing Allure Reports

- Local: [http://localhost:5050/projects/default/reports/latest/index.html](http://localhost:5050/projects/default/reports/latest/index.html)
- GitHub Pages: [https://shlomi10.github.io/RestFullBookerBackend/](https://shlomi10.github.io/RestFullBookerBackend/)

---

## 🔄 CI/CD Pipeline

- GitHub Actions runs on push/PR to `main`
- Generates Allure report
- Publishes report to GitHub Pages

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch  
3. Commit your changes  
4. Open a pull request  
5. Follow conventional commit guidelines

---

## 📜 License

Copyright (c) 2025 Shlomi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---

## 🚧 Future Enhancements

- ❌ Add negative test scenarios  
- 🧵 Enable parallel execution  
- 🚀 Performance & load testing  
- 🌐 Multi-env support  
- 🔔 Slack integration for results
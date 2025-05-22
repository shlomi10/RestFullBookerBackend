# Restful Booker API Tests 🏨

[![Allure](https://img.shields.io/badge/Allure-2.27.0-yellow.svg?style=for-the-badge&logo=allure&logoColor=black)](https://github.com/allure-framework/allure2)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-8.3.5-green.svg?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Docker](https://img.shields.io/badge/Docker-24.0.5-blue.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automation-purple.svg?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)
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

This project is licensed under the [MIT License](LICENSE).

---

## 🚧 Future Enhancements

- ❌ Add negative test scenarios  
- 🧵 Enable parallel execution  
- 🚀 Performance & load testing  
- 🌐 Multi-env support  
- 🔔 Slack integration for results
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PYTHONPATH=/app

WORKDIR /app

# Install only essential OS packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    default-jre \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Allure CLI
RUN curl -L https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz -o allure.tgz && \
    tar -zxvf allure.tgz && \
    mv allure-2.27.0 /opt/allure && \
    ln -s /opt/allure/bin/allure /usr/bin/allure && \
    rm allure.tgz

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project code
COPY . .

# Create folders for results & reports
RUN mkdir -p /app/allure-results /app/allure-report && chmod -R 777 /app/allure-results /app/allure-report

# Default command: run tests + generate HTML report
CMD pytest --alluredir=allure-results && allure generate allure-results --clean -o allure-report

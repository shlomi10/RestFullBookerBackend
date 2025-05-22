import requests
import allure
import logging

log = logging.getLogger(__name__)

class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Create a new booking")
    def create_booking(self, data):
        url = f"{self.base_url}/booking"
        log.info(f"POST {url} with data: {data}")
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
        except requests.RequestException as e:
            log.error(f"Request to {url} failed: {e}")
            raise
        allure.attach(response.text, name="create_booking_response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Retrieve a booking by ID")
    def get_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"
        log.info(f"GET {url}")
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            log.error(f"Request to {url} failed: {e}")
            raise
        allure.attach(response.text, name="get_booking_response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Update an existing booking")
    def update_booking(self, booking_id, data, token):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {"Cookie": f"token={token}"}
        log.info(f"PUT {url} with headers: {headers} and data: {data}")
        try:
            response = requests.put(url, json=data, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            log.error(f"Request to {url} failed: {e}")
            raise
        allure.attach(response.text, name="update_booking_response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Delete a booking")
    def delete_booking(self, booking_id, token):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {"Cookie": f"token={token}"}
        log.info(f"DELETE {url} with headers: {headers}")
        try:
            response = requests.delete(url, headers=headers)
            response.raise_for_status()
        except requests.RequestException as e:
            log.error(f"Request to {url} failed: {e}")
            raise
        allure.attach(response.text, name="delete_booking_response", attachment_type=allure.attachment_type.TEXT)
        return response

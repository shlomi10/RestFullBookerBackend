import time

import pytest
import allure
import logging
import requests
from utils.data_fixtures import booking_data

log = logging.getLogger(__name__)


@allure.suite("Restful Booker API Tests")
@allure.epic("Functionality")
@allure.feature("Room Management")
@allure.story("Validate the Restful Booker API functionality")
class TestBookings:

    @allure.title("Create a new booking")
    @allure.description("This test verifies the ability to create a new booking using the POST /booking endpoint.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "post", "booking")
    def test_create_booking(self, api_client, booking_data):
        response = api_client.create_booking(booking_data)
        assert response.status_code == 200
        assert "bookingid" in response.json()

    @allure.title("Retrieve booking by ID")
    @allure.description("This test checks whether a booking can be retrieved by its ID using GET /booking/{id}.")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.tag("api", "get", "booking")
    def test_get_booking(self, api_client, booking_data):
        booking_id = api_client.create_booking(booking_data).json()["bookingid"]
        response = api_client.get_booking(booking_id)
        assert response.status_code == 200
        assert response.json()["firstname"] == booking_data["firstname"]

    @allure.title("Update an existing booking")
    @allure.description("This test ensures that an existing booking can be updated using PUT /booking/{id}.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "put", "booking")
    def test_update_booking(self, api_client, auth_token, booking_data):
        booking_id = api_client.create_booking(booking_data).json()["bookingid"]
        updated_data = booking_data.copy()
        updated_data["firstname"] = "Updated"
        response = api_client.update_booking(booking_id, updated_data, auth_token)
        assert response.status_code == 200
        assert response.json()["firstname"] == "Updated"

    @allure.title("Delete a booking")
    @allure.description("This test confirms that a booking can be deleted and that it returns 404 after deletion.")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("api", "delete", "booking")
    def test_delete_booking(self, api_client, auth_token, booking_data):
        booking_id = api_client.create_booking(booking_data).json()["bookingid"]
        response = api_client.delete_booking(booking_id, auth_token)
        assert response.status_code == 201
        for _ in range(5):
            try:
                api_client.get_booking(booking_id).raise_for_status()
            except requests.HTTPError as e:
                if e.response.status_code == 404:
                    return  # success: deleted
                raise
            time.sleep(1)

        pytest.fail(f"Booking ID {booking_id} was not deleted after retries")

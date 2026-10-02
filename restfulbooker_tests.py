# restfulbooker_tests.py
# Site: https://restful-booker.herokuapp.com/
# Restful Booker API test cases using requests library.
# Run with: python restfulbooker_tests.py

import requests
import json

BASE_URL = "https://restful-booker.herokuapp.com"

# Test data for creating a booking
booking_payload = {
    "firstname": "John",
    "lastname": "Doe",
    "totalprice": 100,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2024-01-01",
        "checkout": "2024-01-10"
    },
    "additionalneeds": "Breakfast"
}

# Auth token payload
auth_payload = {
    "username": "admin",
    "password": "password123"
}

def test_create_booking():
    """Case 1: Create a new booking (POST)."""
    try:
        response = requests.post(
            f"{BASE_URL}/booking",
            json=booking_payload,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "bookingid" in data
        assert data["booking"]["firstname"] == "John"
        print(f"CASE 1 (create booking): PASS - Booking ID: {data['bookingid']}")
        return data["bookingid"]
    except Exception as error:
        print(f"CASE 1 (create booking): FAIL - {error}")
        return None

def test_get_booking():
    """Case 2: Get a booking by ID (GET)."""
    try:
        # First create a booking to get an ID
        create_response = requests.post(
            f"{BASE_URL}/booking",
            json=booking_payload,
            headers={"Content-Type": "application/json"}
        )
        booking_id = create_response.json()["bookingid"]
        
        # Now get the booking
        get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["firstname"] == "John"
        assert data["lastname"] == "Doe"
        print(f"CASE 2 (get booking): PASS - Booking ID: {booking_id}")
        return booking_id
    except Exception as error:
        print(f"CASE 2 (get booking): FAIL - {error}")
        return None

def test_get_nonexistent_booking():
    """Case 3: Get a booking that doesn't exist (GET)."""
    try:
        response = requests.get(f"{BASE_URL}/booking/99999")
        assert response.status_code == 404
        print("CASE 3 (get nonexistent booking): PASS")
    except Exception as error:
        print(f"CASE 3 (get nonexistent booking): FAIL - {error}")

def test_update_booking_put():
    """Case 4: Update a booking completely (PUT)."""
    try:
        # Create a booking first
        create_response = requests.post(
            f"{BASE_URL}/booking",
            json=booking_payload,
            headers={"Content-Type": "application/json"}
        )
        booking_id = create_response.json()["bookingid"]
        
        # Get auth token
        auth_response = requests.post(
            f"{BASE_URL}/auth",
            json=auth_payload,
            headers={"Content-Type": "application/json"}
        )
        token = auth_response.json()["token"]
        
        # Update the booking with PUT
        updated_payload = {
            "firstname": "Jane",
            "lastname": "Smith",
            "totalprice": 200,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2024-02-01",
                "checkout": "2024-02-15"
            },
            "additionalneeds": "Lunch"
        }
        update_response = requests.put(
            f"{BASE_URL}/booking/{booking_id}",
            json=updated_payload,
            headers={
                "Content-Type": "application/json",
                "Cookie": f"token={token}"
            }
        )
        assert update_response.status_code == 200
        data = update_response.json()
        assert data["firstname"] == "Jane"
        assert data["totalprice"] == 200
        print(f"CASE 4 (update booking PUT): PASS - Booking ID: {booking_id}")
    except Exception as error:
        print(f"CASE 4 (update booking PUT): FAIL - {error}")

def test_update_booking_patch():
    """Case 5: Partially update a booking (PATCH)."""
    try:
        # Create a booking first
        create_response = requests.post(
            f"{BASE_URL}/booking",
            json=booking_payload,
            headers={"Content-Type": "application/json"}
        )
        booking_id = create_response.json()["bookingid"]
        
        # Get auth token
        auth_response = requests.post(
            f"{BASE_URL}/auth",
            json=auth_payload,
            headers={"Content-Type": "application/json"}
        )
        token = auth_response.json()["token"]
        
        # Partial update with PATCH
        patch_payload = {"totalprice": 150}
        patch_response = requests.patch(
            f"{BASE_URL}/booking/{booking_id}",
            json=patch_payload,
            headers={
                "Content-Type": "application/json",
                "Cookie": f"token={token}"
            }
        )
        assert patch_response.status_code == 200
        data = patch_response.json()
        assert data["totalprice"] == 150
        assert data["firstname"] == "John"  # Should remain unchanged
        print(f"CASE 5 (update booking PATCH): PASS - Booking ID: {booking_id}")
    except Exception as error:
        print(f"CASE 5 (update booking PATCH): FAIL - {error}")

def test_delete_booking():
    """Case 6: Delete a booking (DELETE)."""
    try:
        # Create a booking first
        create_response = requests.post(
            f"{BASE_URL}/booking",
            json=booking_payload,
            headers={"Content-Type": "application/json"}
        )
        booking_id = create_response.json()["bookingid"]
        
        # Get auth token
        auth_response = requests.post(
            f"{BASE_URL}/auth",
            json=auth_payload,
            headers={"Content-Type": "application/json"}
        )
        token = auth_response.json()["token"]
        
        # Delete the booking
        delete_response = requests.delete(
            f"{BASE_URL}/booking/{booking_id}",
            headers={
                "Content-Type": "application/json",
                "Cookie": f"token={token}"
            }
        )
        assert delete_response.status_code == 201
        
        # Verify it's deleted
        get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_response.status_code == 404
        print(f"CASE 6 (delete booking): PASS - Booking ID: {booking_id}")
    except Exception as error:
        print(f"CASE 6 (delete booking): FAIL - {error}")

def test_auth_token_success():
    """Case 7: Get auth token with valid credentials."""
    try:
        response = requests.post(
            f"{BASE_URL}/auth",
            json=auth_payload,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert len(data["token"]) > 0
        print(f"CASE 7 (auth token success): PASS - Token: {data['token'][:10]}...")
    except Exception as error:
        print(f"CASE 7 (auth token success): FAIL - {error}")

def test_auth_token_invalid():
    """Case 8: Get auth token with invalid credentials."""
    try:
        invalid_payload = {"username": "wrong", "password": "wrong"}
        response = requests.post(
            f"{BASE_URL}/auth",
            json=invalid_payload,
            headers={"Content-Type": "application/json"}
        )
        assert response.status_code == 403
        print("CASE 8 (auth token invalid): PASS")
    except Exception as error:
        print(f"CASE 8 (auth token invalid): FAIL - {error}")

def test_update_without_auth():
    """Case 9: Try to update without auth token (should fail)."""
    try:
        # Create a booking first
        create_response = requests.post(
            f"{BASE_URL}/booking",
            json=booking_payload,
            headers={"Content-Type": "application/json"}
        )
        booking_id = create_response.json()["bookingid"]
        
        # Try to update without token
        patch_payload = {"totalprice": 999}
        patch_response = requests.patch(
            f"{BASE_URL}/booking/{booking_id}",
            json=patch_payload,
            headers={"Content-Type": "application/json"}
        )
        assert patch_response.status_code == 403
        print(f"CASE 9 (update without auth): PASS - Booking ID: {booking_id}")
    except Exception as error:
        print(f"CASE 9 (update without auth): FAIL - {error}")

def test_health_check():
    """Case 10: API health check."""
    try:
        response = requests.get(f"{BASE_URL}/ping")
        assert response.status_code == 200
        assert response.text == "Created for Qxf2"
        print("CASE 10 (health check): PASS")
    except Exception as error:
        print(f"CASE 10 (health check): FAIL - {error}")

if __name__ == "__main__":
    print("Running Restful Booker API Tests...\n")
    test_health_check()
    test_create_booking()
    test_get_booking()
    test_get_nonexistent_booking()
    test_update_booking_put()
    test_update_booking_patch()
    test_delete_booking()
    test_auth_token_success()
    test_auth_token_invalid()
    test_update_without_auth()
    print("\nAll tests completed!")

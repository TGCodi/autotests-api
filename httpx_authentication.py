import httpx

login_payload = {
    "email": "1user1@example.com",
    "password": "1user1"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()


print(f"Login response {login_response_data}")
print(f"Status code {login_response.status_code}")

refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

print(f"Refresh token response {refresh_response_data}")
print(f"Status code {refresh_response.status_code}")

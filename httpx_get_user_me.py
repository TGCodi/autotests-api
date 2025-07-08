import httpx


# Token
login_payload = {
    "email": "1user1@example.com",
    "password": "1user1"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print(login_response.status_code)
print(login_response_data)

access_token_payload = {
    "access_token": login_response_data["token"]["accessToken"]
}

headers = {
    "Authorization": f"Bearer {access_token_payload['access_token']}"
}

get_me = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print(get_me.status_code)
print(get_me.json())

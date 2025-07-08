import httpx

from tools.fakers import get_random_email

create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user:", create_user_response)

login_user_payload = {
    "email": "1user1@example.com",
    "password": "1user1"
}
login_user_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_user_payload)
login_user_response_data = login_user_response.json()
print("Login data:", login_user_response_data)

update_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
update_user_headers = {
    "Authorization": f"Bearer {login_user_response_data["token"]["accessToken"]}"
}
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
    headers=update_user_headers,
    json=update_user_payload,
)
update_user_response_data = update_user_response.json()
print("Update User data:", update_user_response_data)
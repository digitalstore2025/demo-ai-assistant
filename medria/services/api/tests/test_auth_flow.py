from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_signup_and_login_flow():
    email = "test-user@example.com"
    password = "secret123"

    signup_response = client.post(
        "/auth/signup",
        json={"email": email, "password": password, "role": "patient", "language": "ar"},
    )
    assert signup_response.status_code == 200

    login_response = client.post(
        "/auth/login",
        json={"email": email, "password": password},
    )
    assert login_response.status_code == 200
    body = login_response.json()
    assert body["access_token"]

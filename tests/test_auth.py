# tests/test_auth.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_user_ok():
    response = client.post(
        "/api/auth/register",
        json={
            "nombre": "Test User",
            "email": "testuser_unique@example.com",
            "password": "supersecure"
        }
    )
    assert response.status_code == 200
    assert "id" in response.json()

    data = response.json()
    assert "id" in data
    assert data["email"] == "testuser@example.com"

def test_register_user_duplicate_email():
    # Intentar registrar con el mismo correo
    response = client.post(
        "/api/auth/register",
        json={
            "nombre": "Test User",
            "email": "testuser@example.com",
            "password": "supersecure"
        }
    )
    assert response.status_code == 409  # O 400, según tu manejo

def test_login_ok():
    response = client.post(
        "/api/auth/login",
        data={
            "username": "testuser@example.com",
            "password": "supersecure"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_login_wrong_password():
    response = client.post(
        "/api/auth/login",
        data={
            "username": "testuser@example.com",
            "password": "wrongpassword"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid credentials"

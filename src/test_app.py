from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_get_activities_returns_list():
    response = client.get("/activities")
    assert response.status_code == 200
    assert "Chess Club" in response.json()


def test_get_single_activity_returns_details():
    response = client.get("/activities/Chess%20Club")
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "Learn strategies and compete in chess tournaments"


def test_signup_for_activity_requires_valid_email():
    response = client.post("/activities/Chess%20Club/signup", json={"email": "invalid-email"})
    assert response.status_code == 422

from fastapi.testclient import TestClient

from src.main2 import app


def test_create_user_endpoint():
    client = TestClient(app)

    response = client.post(
        "/users",
        json={
            "first_name": "Abdelhakim",
            "last_name": "Berrim",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "full_name": "Abdelhakim Berrim"
    }

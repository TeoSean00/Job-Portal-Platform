from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_placeholder():
    assert True

def test_create_role_listing():
    response = client.post(
        "/api/role_listing",
        json={
            "role_listing_desc": "This is a description of the role",
            "role_listing_open": "22-02-2021",
            "role_listing_close": "22-03-2021",
            "role_listing_creator": "Admin1", 
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Created!"
    }

if __name__ == "__main__":
    pytest.main()

    

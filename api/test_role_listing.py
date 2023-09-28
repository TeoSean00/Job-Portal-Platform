from fastapi.testclient import TestClient
from main import app, User, RoleListing

client = TestClient(app)

def test_success_create_role_listing():
    # Arrange
    user = User(user_token=1234, role="1")
    role_details = RoleListing(
        role_name="Test Role",
        role_listing_desc="This is a test role",
        role_listing_source=1,
        role_listing_open="2022-01-01T00:00:00",
        role_listing_close="2022-01-31T23:59:59",
        role_listing_creator=1
    )

    # Act
    response = client.post("/api/role_listing", json={"user": user.model_dump(), "role_details": role_details.model_dump()})

    # Assert
    assert response.status_code == 201
    assert response.json() == {"message": "Created!"}

def test_unauthorized_create_role_listing():
    # Arrange
    user = User(user_token=1234, role="4")
    role_details = RoleListing(
        role_name="Test Role",
        role_listing_desc="This is a test role",
        role_listing_source=1,
        role_listing_open="2022-01-01T00:00:00",
        role_listing_close="2022-01-31T23:59:59",
        role_listing_creator=1
    )

    # Act
    response = client.post("/api/role_listing", json={"user": user.model_dump(), "role_details": role_details.model_dump()})

    # Assert
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized user!"}

def test_invalid_create_role_listing():
    user = User(user_token=1234, role="2")
    role_details = RoleListing(
        role_name="Invalid Role",
        role_listing_desc="This is a test role",
        role_listing_source=1,
        role_listing_open="2022-01-01T00:00:00",
        role_listing_close="2022-01-31T23:59:59",
        role_listing_creator=1
    )

    # Act
    response = client.post("/api/role_listing", json={"user": user.model_dump(), "role_details": role_details.model_dump()})
    print(response.json())
    # Assert
    assert response.status_code == 400
    assert response.json() == {'detail': {'message': 'Invalid role details!'}}
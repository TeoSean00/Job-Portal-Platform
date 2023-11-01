import os
import sys
from unittest.mock import call, patch

import pytest
from fastapi.testclient import TestClient

import api.routers.common_services as common_services
from api.main import app
from database.schemas import RoleListingsPydantic, User

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
client = TestClient(app)

# Integraton testing workflow
# CRU Of role listings

# Steps taken
# Create a role listing
# Query role listing
# Update role listing
# delete role listing


class TestIntegration:
    @pytest.fixture(autouse=True)
    def setup(self):
        """
        Health check first.
        """
        # Asserting that backend and database is working
        print("Testing health")
        healthcheck = client.get("/api/healthcheck")
        assert healthcheck.status_code == 200
        assert (
            healthcheck.json().get("database")
            == "Database connection successful!"
        )

    def test_cru_role_listing(self):
        # ========================== Headers ==========================
        headers = {
            "role": "hr",
            "updater-staff-id": "123456787",
        }

        role_id = 234511581
        role_listing_id = 999666999

        # Deleting to clear, if not found will not crash.
        delete_role_listing = client.delete(
            f"/api/role/role_listing/{role_listing_id}", headers=headers
        )
        # ========================== Read ==========================

        # Get all role details
        role_details = client.get(
            f"/api/role/role_details?role_id={role_id}", headers=headers
        )
        # Assert that there is a response
        assert role_details.status_code == 200
        # Assert that there is an existing role detail
        assert role_details.json().get("role_details") is not None
        print(
            f"CRU RoleListing: Successfully queried role details of {role_id}."
        )

        # ========================== Create ==========================
        create_role_listing_body = {
            "role_listing_id": role_listing_id,
            "role_id": role_id,
            "role_listing_desc": "Role created for integration testing.",
            "role_listing_source": 123456786,
            "role_listing_open": "2023-10-22T16:00:00",
            "role_listing_creator": 123456786,
            "role_department": "Role created for integration testing.",
            "role_location": "Role created for integration testing.",
        }

        # Create a role listing
        role_listing = client.post(
            "/api/role/role_listing",
            json=create_role_listing_body,
            headers=headers,
        )
        print(role_listing.json())
        # Assert that there is a response
        assert role_listing.status_code == 201
        assert role_listing.json() == {"message": "Created!"}
        print(
            f"CRU RoleListing: Successfully created role listing {role_listing_id}."
        )

        # ========================== Update ==========================
        role_listing = client.get(
            f"/api/role/role_listing?role_listing_id={role_listing_id}",
            headers=headers,
        )

        # Assert that there is a response
        assert role_listing.status_code == 200
        # Assert that there is an existing role listing
        assert role_listing.json().get("role_listing") is not None
        print("CRU RoleListing: Successfully queried created role listing.")

        # Update role listing
        update_role_listing_body = role_listing.json()["role_listing"]
        update_role_listing_body["role_listing"][
            "role_listing_desc"
        ] = "Updated text!"

        role_listing = client.put(
            "/api/role/role_listing",
            json=update_role_listing_body["role_listing"],
            headers=headers,
        )
        assert role_listing.status_code == 200
        assert role_listing.json() == {"message": "Updated!"}

        # Query role listing to check update
        role_listing = client.get(
            f"/api/role/role_listing?role_listing_id={role_listing_id}",
            headers=headers,
        )
        # Assert that there is a response
        assert role_listing.status_code == 200
        assert (
            role_listing.json()["role_listing"]["role_listing"][
                "role_listing_desc"
            ]
            == "Updated text!"
        )
        print("CRU RoleListing: Successfully updated created role listing.")

        # ========================== Delete ==========================
        delete_role_listing = client.delete(
            f"/api/role/role_listing/{role_listing_id}", headers=headers
        )
        # Assert that there is a response
        assert delete_role_listing.status_code == 200

        # Assert that it is deleted
        role_listing = client.get(
            f"/api/role/role_listing?role_listing_id={role_listing_id}",
            headers=headers,
        )
        assert role_listing.status_code == 404
        print(
            f"CRU RoleListing: Successfully cleaned up role listing {role_listing_id}."
        )
        print("CRU RoleListing: Successfully completed.")

    # def test_view_skills_of_applicants():
    #     pass

    # def test_browse_and_filter_role_listing():
    #     # Get all role listings info
    #     role_listings = client.get("/role/role_listings_info")
    #     assert role_listings.status_code == 200
    #     assert role_listings.json().get("role_listings_info") is not None
    #     # Filtering is done on front end so

    # def test_role_skill_match():
    #     # This seems to just call /role-skills-match, not rly an integration testing?
    #     pass

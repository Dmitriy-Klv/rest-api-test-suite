import pytest


class TestPostsCRUD:

    @pytest.fixture
    def new_post_payload(self):
        return {
            "title": "test title",
            "body": "test body",
            "userId": 1
        }

    def test_create_post(self, post_client, new_post_payload):
        response = post_client.create_post(new_post_payload)

        assert response.status_code == 201

        data = response.json()
        assert data["title"] == new_post_payload["title"]
        assert data["body"] == new_post_payload["body"]
        assert data["userId"] == new_post_payload["userId"]
        assert "id" in data

    def test_get_post(self, post_client):
        response = post_client.get_post(1)

        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_update_post_put(self, post_client):
        updated_payload = {
            "id": 1,
            "title": "updated title",
            "body": "updated body",
            "userId": 1
        }

        response = post_client.put("/posts/1", json=updated_payload)

        assert response.status_code == 200

        data = response.json()
        assert data["title"] == "updated title"
        assert data["body"] == "updated body"

    def test_update_post_patch(self, post_client):
        patch_payload = {
            "title": "patched title"
        }

        response = post_client.patch("/posts/1", json=patch_payload)

        assert response.status_code == 200
        assert response.json()["title"] == "patched title"

    def test_delete_post(self, post_client):
        response = post_client.delete("/posts/1")

        assert response.status_code in (200, 204)

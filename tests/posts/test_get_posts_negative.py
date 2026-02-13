
class TestPostsNegative:


    def test_get_non_existent_post(self, post_client):
        response = post_client.get_post(999999)
        assert response.status_code == 404

    def test_get_post_with_string_id(self, post_client):
        response = post_client.get_post("wrong-id-format")
        assert response.status_code == 404

    def test_delete_non_existent_post(self, post_client):
        response = post_client.delete_post(999999)
        assert response.status_code < 500

    def test_create_post_with_empty_title(self, post_client):
        payload = {
            "title": "",
            "body": "test body",
            "userId": 1
        }
        response = post_client.create_post(payload)
        assert response.status_code == 201

    def test_patch_post_with_invalid_user_id(self, post_client):
        payload = {"userId": "not-an-integer"}
        response = post_client.patch_post(1, payload)
        assert response.status_code < 500
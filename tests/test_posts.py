from http.client import responses

from api.post_client import PostClient
from models.post_model import Post


class TestPosts:
    def setup_method(self):
        self.post_client = PostClient()

    def test_get_post_1_status_code(self):
        response = self.post_client.get_post(1)
        assert response.status_code == 200

    def test_get_post_1_data_validation(self):
        response = self.post_client.get_post(1)
        data = response.json()

        post = Post(**data)

        assert post.id == 1
        assert isinstance(post.title, str)
        assert len(post.title) > 0

    def test_get_non_existent_post_returns_404(self):
        response = self.post_client.get_post(9999)

        assert response.status_code == 404

    def test_get_post_2_status_code(self):
        response = self.post_client.get_post(2)
        assert response.status_code == 200

    def test_get_post_2_data_validation(self):
        response = self.post_client.get_post(2)
        data = response.json()

        post = Post(**data)

        assert post.id == 1
        assert post.user_id == 2
        assert isinstance(post.title, str)
        assert len(post.title) > 0

    def test_get_post_3_status_code(self):
        response = self.post_client.get_post(3)
        assert response.status_code == 200

    def test_get_post_3_data_validation(self):
        response = self.post_client.get_post(3)
        data = response.json()

        post = Post(**data)

        assert post.id == 3
        assert post.user_id == 1
        assert isinstance(post.title, str)
        assert len(post.title) > 0

from api.post_client import PostClient
from models.post_model import Post


class TestPosts:
    def setup_method(self):
        self.post_client = PostClient()

    def test_get_single_post_status_code(self):
        response = self.post_client.get_post(1)
        assert response.status_code == 200

    def test_get_single_post_data_validation(self):
        response = self.post_client.get_post(1)
        data = response.json()

        post = Post(**data)

        assert post.id == 1
        assert isinstance(post.title, str)
        assert len(post.title) > 0

    def test_get_non_existent_post_returns_404(self):
        response = self.post_client.get_post(9999)

        assert response.status_code == 404
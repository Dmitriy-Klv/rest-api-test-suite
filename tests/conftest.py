import pytest
from api.post_client import PostClient
from models.post_model import Post


@pytest.fixture
def post_client():
    return PostClient()


@pytest.fixture
def get_post(post_client):
    def _get_post(post_id: int, expected_status: int = 200):
        response = post_client.get_post(post_id)
        assert response.status_code == expected_status
        return response
    return _get_post


@pytest.fixture
def valid_post(get_post):
    def _valid_post(post_id: int):
        response = get_post(post_id)
        return Post(**response.json())
    return _valid_post

import pytest
from api.post_client import PostClient
from models.post_model import Post
import time
import random

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


@pytest.fixture(autouse=True, scope="function")
def slow_down_tests():
    yield

    delay = random.uniform(0.2, 0.8)
    time.sleep(delay)
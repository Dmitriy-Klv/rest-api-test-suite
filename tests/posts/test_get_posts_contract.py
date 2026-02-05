import pytest
from models.post_model import Post


@pytest.mark.parametrize("post_id", range(1, 5))
def test_post_contract(get_post, post_id):
    response = get_post(post_id)

    Post(**response.json())

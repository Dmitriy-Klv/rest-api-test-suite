import pytest


@pytest.mark.parametrize("post_id", range(1, 5))
def test_post_data_validation(valid_post, post_id):
    post = valid_post(post_id)

    assert post.id > 0
    assert post.user_id > 0
    assert post.title.strip() != ""
    assert post.body.strip() != ""

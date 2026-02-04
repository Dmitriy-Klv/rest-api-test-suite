import pytest


class TestPosts:

    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post_status_code(self, get_post, post_id):
        get_post(post_id)

    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post_data_validation(self, valid_post, post_id):
        post = valid_post(post_id)

        assert post.id == post_id
        assert isinstance(post.title, str)
        assert post.title
        assert isinstance(post.user_id, int)
        assert post.user_id > 0

    def test_get_non_existent_post_returns_404(self, get_post):
        get_post(9999, expected_status=404)

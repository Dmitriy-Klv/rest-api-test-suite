
def test_get_post_not_found(get_post):
    get_post(9999, expected_status=404)


def test_get_post_invalid_id(post_client):
    response = post_client.get_post("abc")
    assert response.status_code in (400, 404)

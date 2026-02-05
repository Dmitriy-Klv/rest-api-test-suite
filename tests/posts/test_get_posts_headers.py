
def test_post_headers(get_post):
    response = get_post(1)

    assert response.headers["Content-Type"].startswith(
        "application/json"
    )

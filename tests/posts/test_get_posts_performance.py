

def test_post_response_time(get_post):
    response = get_post(1)

    assert response.elapsed.total_seconds() < 1

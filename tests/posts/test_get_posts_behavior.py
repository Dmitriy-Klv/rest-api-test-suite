

def test_get_post_consistency(valid_post):
    post1 = valid_post(1)
    post2 = valid_post(1)

    assert post1 == post2

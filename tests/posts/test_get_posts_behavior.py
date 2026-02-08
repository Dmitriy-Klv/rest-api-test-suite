

def test_get_post_consistency(valid_post):
    post_first = valid_post(1)
    post_second = valid_post(1)

    assert post_first.id == post_second.id
    assert post_first.user_id == post_second.user_id
    assert post_first.title == post_second.title
    assert post_first.body == post_second.body


from lib.comment import Comment

def test_creates_comment():
    # Given a set of data
    # It creates a Comment object containing this data.
    comment = Comment(1, "Test username", "Test comment", 1)
    assert comment.id == 1
    assert comment.username == "Test username"
    assert comment.comment_content == "Test comment"
    assert comment.post_id == 1

def test_compares_comments():
    # Given two Comment objects
    # It comepares the contents of these objects.
    comment_1 = Comment(1, "Test username", "Test comment", 1)
    comment_2 = Comment(1, "Test username", "Test comment", 1)
    assert comment_1 == comment_2

def test_returns_contents_when_called():
    # Given a Comment object
    # It returns the contents of the object as a string when called.
    comment = Comment(1, "Test username", "Test comment", 1)
    assert str(comment) == "1, Test username, Test comment, 1"

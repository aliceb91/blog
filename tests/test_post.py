from lib.post import Post
from unittest.mock import Mock

def test_creates_post():
    # Given a set of data
    # It creates a Post object containing this data.
    comment_1 = Mock()
    comment_2 = Mock()
    post = Post(1, "Test title", "Test content", [comment_1, comment_2])
    assert post.id == 1
    assert post.title == "Test title"
    assert post.post_content == "Test content"
    assert post.post_comments == [comment_1, comment_2]

def test_compares_comments():
    # Given two Post objects
    # It comepares the contents of these objects.
    comment_1 = Mock()
    comment_2 = Mock()
    post_1 = Post(1, "Test title", "Test content", [comment_1, comment_2])
    post_2 = Post(1, "Test title", "Test content", [comment_1, comment_2])
    assert post_1 == post_2

def test_returns_contents_when_called():
    # Given a Post object
    # It returns the contents of the object as a string when called.
    comment_1 = Mock()
    comment_1.id = 1
    comment_1.username = "Mock username 1"
    comment_1.comment_content = "Test content 1"
    comment_1.post_id = 1

    comment_2 = Mock()
    comment_2.id = 2
    comment_2.username = "Mock username 2"
    comment_2.comment_content = "Test content 2"
    comment_2.post_id = 1

    comment = Post(1, "Test title", "Test content", [comment_1, comment_2])
    assert str(comment) == "1, Test title, Test content, Mock username 1: Test content 1, Mock username 2: Test content 2"

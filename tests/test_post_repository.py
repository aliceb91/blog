from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment

def test_returns_post_with_comments(db_connection):
    # Given a database of posts and comments
    # It returns a single post with all relevent comments.
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)
    test_comment_1 = Comment(7, "11am Enjoyer", "I like this!", 4)
    test_comment_2 = Comment(8, "11am Hater", "I hate this!", 4)
    post_with_comments = repository.post_with_comments(4)
    test_post = Post(4, "11am", "The time is 11am", [test_comment_1, test_comment_2])
    assert post_with_comments == test_post

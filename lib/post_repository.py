
from lib.post import Post
from lib.comment import Comment

class PostRepository():
    def __init__(self, connection):
        # Stores connection data.
        #
        # Parameters:
        #   _connection: a Connection object.
        self._connection = connection

    def post_with_comments(self, post_id):
        # Fetches a post from the database with all associated comments.
        #
        # Parameters:
        #   post_id: int
        #
        # Returns:
        #   A Post object containing a list of Comment objects.
        #
        # Side effects:
        #   None.
        rows = self._connection.execute(
            '''
            SELECT comments.id AS comments_id, comments.username, comments.comment_content, comments.post_id, posts.id AS posts_id, posts.title, posts.post_content
            FROM comments JOIN posts
            ON comments.post_id = posts.id
            WHERE posts.id = %s''', [post_id]
        )
        comments = []
        for row in rows:
            comment = Comment(row['comments_id'], row['username'], row['comment_content'], row['post_id'])
            comments.append(comment)
        return Post(rows[0]['posts_id'], rows[0]['title'], rows[0]['post_content'], comments)

from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog.sql")

# Retrieve all artists
post_repository = PostRepository(connection)
post_with_comments = post_repository.post_with_comments(4)

# List them out
print(post_with_comments)

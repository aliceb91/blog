class Comment():
    def __init__(self, id, username, comment_content, post_id):
        # Creates a Comment object based on the provided parameters.
        #
        # Parameters:
        #   id: int
        #   username: string
        #   comment_content: string
        #   post_id: int
        self.id = id
        self.username = username
        self.comment_content = comment_content
        self.post_id = post_id

    def __eq__(self, other):
        # Compares the contents of two Comment objects.
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Returns the contents of the object when the object is called.
        return f"{self.id}, {self.username}, {self.comment_content}, {self.post_id}"

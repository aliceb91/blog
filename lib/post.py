class Post():
    def __init__(self, id, title, post_content, post_comments):
        # Creates a Post object based on the provided parameters.
        #
        # Parameters:
        #   id: int
        #   title: string
        #   post_content: string
        #   post_comments: list of Comment objects
        self.id = id
        self.title = title
        self.post_content = post_content
        self.post_comments = post_comments

    def __eq__(self, other):
        # Compares the contents of two Post objects.
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Returns the contents of the object when the object is called.
        comments = ""
        for comment in self.post_comments:
            comments += ", " + comment.username + ": " + comment.comment_content
        return f"{self.id}, {self.title}, {self.post_content}{comments}"

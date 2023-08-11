# User Story
```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.
```

# Nouns
post, title, post_content, comments, comment_content, username

# Column Table
| Record                | Properties                |
| --------------------- | ------------------------- |
| posts                 | title, post_content       |
| comments              | comment_content, username |

# Column Types
```
posts:
    id: SERIAL
    title: text
    post_content: text

comments:
    id: SERIAL
    username: text
    comment_content: text
```

# Table Relationship
Can one post have many comments? YES\
Can one comment have many posts? NO\

-> Therefore,\
-> A post has many comments\
-> A comment belongs to a post\

-> Therefore, the foreign key is on the comments table
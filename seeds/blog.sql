DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    post_content text
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    username text,
    comment_content text,
    post_id int,
    constraint fk_post foreign key(post_id)
        references posts(id)
        on delete cascade
);

INSERT INTO posts (title, post_content) VALUES ('8am', 'The time is 8am');
INSERT INTO posts (title, post_content) VALUES ('9am', 'The time is 9am');
INSERT INTO posts (title, post_content) VALUES ('10am', 'The time is 10am');
INSERT INTO posts (title, post_content) VALUES ('11am', 'The time is 11am');

INSERT INTO comments (username, comment_content, post_id) VALUES ('8am Enjoyer', 'I like this!', 1);
INSERT INTO comments (username, comment_content, post_id) VALUES ('8am Hater', 'I hate this!', 1);
INSERT INTO comments (username, comment_content, post_id) VALUES ('9am Enjoyer', 'I like this!', 2);
INSERT INTO comments (username, comment_content, post_id) VALUES ('9am Hater', 'I hate this!', 2);
INSERT INTO comments (username, comment_content, post_id) VALUES ('10am Enjoyer', 'I like this!', 3);
INSERT INTO comments (username, comment_content, post_id) VALUES ('10am Hater', 'I hate this!', 3);
INSERT INTO comments (username, comment_content, post_id) VALUES ('11am Enjoyer', 'I like this!', 4);
INSERT INTO comments (username, comment_content, post_id) VALUES ('11am Hater', 'I hate this!', 4);
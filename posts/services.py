from .models import Post, Comment

def add_comment_to_post(post: Post, author_name: str, body: str) -> Comment:
    if not body or not body.strip():
        raise ValueError("Comment body cannot be empty")
    comment = Comment.objects.create(post=post, author_name=author_name[:150], body=body.strip())
    return comment

## Comment System Documentation

### Overview
Authenticated users can post, edit, and delete comments on blog posts.
All visitors can read comments.

### Rules
- Only logged-in users can create comments.
- Only the comment's **author** can edit or delete it.
- Deleting a post also deletes all its comments (CASCADE).

### URLs
| Action         | URL                                    |
|----------------|----------------------------------------|
| Add comment    | /posts/<post_id>/comments/new/         |
| Edit comment   | /comments/<comment_id>/edit/           |
| Delete comment | /comments/<comment_id>/delete/         |

This project is part of the ALX Django learning lab.
It demonstrates the basic setup of a Django project.
# Permissions and Groups Setup

### Groups Created:
- **Viewers**: Can only view book lists (`can_view`).
- **Editors**: Can view, create, and edit books (`can_view`, `can_create`, `can_edit`).
- **Admins**: Full CRUD access (`can_view`, `can_create`, `can_edit`, `can_delete`).

### Implementation:
Permissions are defined in `bookshelf/models.py` under `Book.Meta`. 
Access is restricted in `bookshelf/views.py` using the `@permission_required` decorator.
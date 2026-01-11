book.delete()
# CRUD Operations in Django Shell
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()

## Delete
>>> b.delete()
(1, {'book_store.Book': 1})
>>> Book.objects.all()
<QuerySet []>
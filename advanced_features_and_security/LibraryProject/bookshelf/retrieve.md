# CRUD Operations in Django Shell
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book


## Retrieve
>>> Book.objects.all()
<QuerySet [<Book: Dune by Frank Herbert>]>

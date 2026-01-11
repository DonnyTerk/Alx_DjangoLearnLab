# CRUD Operations in Django Shell
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book



## Update
>>> b = Book.objects.get(title="Dune")
>>> b.title = "Dune: Deluxe Edition"
>>> b.save()
>>> b.title
'Dune: Deluxe Edition'

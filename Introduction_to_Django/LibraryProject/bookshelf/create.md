# CRUD Operations in Django Shell

```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

## Create
>>> from book_store.models import Book
>>> book1 = Book.objects.create(title="Dune", author="Frank Herbert", publication_year=1965)
<Book: Dune by Frank Herbert>

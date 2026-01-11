# CRUD Operations in Django Shell

## Create
>>> from book_store.models import Book
>>> book1 = Book.objects.create(title="Dune", author="Frank Herbert", publication_year=1965)
<Book: Dune by Frank Herbert>

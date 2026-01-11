# CRUD Operations in Django Shell

## Create
>>> from book_store.models import Book
>>> book1 = Book.objects.create(title="Dune", author="Frank Herbert", publication_year=1965)
<Book: Dune by Frank Herbert>

## Read
>>> Book.objects.all()
<QuerySet [<Book: Dune by Frank Herbert>]>

## Update
>>> b = Book.objects.get(title="Dune")
>>> b.title = "Dune: Deluxe Edition"
>>> b.save()
>>> b.title
'Dune: Deluxe Edition'

## Delete
>>> b.delete()
(1, {'book_store.Book': 1})
>>> Book.objects.all()
<QuerySet []>
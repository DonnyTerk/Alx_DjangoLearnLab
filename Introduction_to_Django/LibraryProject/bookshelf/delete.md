book.delete()
# CRUD Operations in Django Shell
# Delete the book
single_book.delete()
# Verify it's gone (should return an empty QuerySet)
print(Book.objects.all())

## Delete
>>> b.delete()
(1, {'book_store.Book': 1})
>>> Book.objects.all()
<QuerySet []>
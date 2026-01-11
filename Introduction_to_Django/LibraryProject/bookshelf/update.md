# CRUD Operations in Django Shell

## Update
>>> b = Book.objects.get(title="Dune")
>>> b.title = "Dune: Deluxe Edition"
>>> b.save()
>>> b.title
'Dune: Deluxe Edition'

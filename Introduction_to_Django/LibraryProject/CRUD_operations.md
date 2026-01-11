#create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book


from bookshelf.models import Book
Book.objects.all()



from bookshelf.models import Book
Book.objects.all()



book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book



book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()



Book.objects.all()


book.title = "Nineteen Eighty-Four"
book.save()


book.delete()


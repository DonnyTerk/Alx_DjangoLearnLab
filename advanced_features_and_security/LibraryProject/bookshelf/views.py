from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# VIEW: can_view
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# CREATE: can_create
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        # logic to save book
        return redirect('book_list')
    return render(request, 'bookshelf/form_book.html')

# EDIT: can_edit
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # logic to update book
        return redirect('book_list')
    return render(request, 'bookshelf/form_book.html', {'book': book})

# DELETE: can_delete
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

from django.shortcuts import render
from .models import Book
from .forms import ExampleForm

def search_books(request):
    query = request.GET.get('q', '')
    
    # SECURE: Using Django's ORM automatically parameterizes the query
    # This prevents SQL Injection attacks.
    books = Book.objects.filter(title__icontains=query)
    
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_form_view(request):
    # SECURE: Using Django Forms for validation and sanitization
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process sanitized data
            pass
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

from django.shortcuts import render
from .forms import ExampleForm

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Data is now "cleaned" and safe from script injection
            cleaned_data = form.cleaned_data
            # Process data...
            return render(request, 'bookshelf/form_example.html', {'form': form, 'success': True})
    else:
        form = ExampleForm()
        
    return render(request, 'bookshelf/form_example.html', {'form': form})

from django.shortcuts import render
from .forms import ExampleForm

def example_form_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
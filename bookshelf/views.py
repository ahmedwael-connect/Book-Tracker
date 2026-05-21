from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


# Create your views here.
# 1. DASHBOARD VIEW
def dashboard(request):
    # Query database and filter books based on status
    to_read_books = Book.objects.filter(status='TO_READ')
    reading_books = Book.objects.filter(status='READING')
    completed_books = Book.objects.filter(status='COMPLETED')

    # Context is a dictionary that carries database variables over to the HTML template
    context = {
        'to_read': to_read_books,
        'reading': reading_books,
        'completed': completed_books,
    }
    return render(request, 'bookshelf/dashboard.html', context)


# 2. FAVORITES VIEW (Only 5-star books)
def favorites(request):
    # Filter books where rating is exactly 5
    fav_books = Book.objects.filter(rating=5)
    return render(request, 'bookshelf/favorites.html', {'favorites': fav_books})


# 3. ADD BOOK VIEW
def add_book(request):
    if request.method == 'POST':
        # If the user submitted the form, populate the BookForm with the submitted data
        form = BookForm(request.POST)
        if form.is_valid():
            # If the data entered is correct, save it directly to the database
            form.save()
            return redirect('dashboard')
    else:
        # If they just visited the page, give them a blank form
        form = BookForm()

    return render(request, 'bookshelf/add_book.html', {'form': form})


# 4. QUICK ACTION: START READING (To Read -> Reading)
def start_reading(request, book_id):
    # Fetch the book by its unique ID. If not found, show a 404 Error page.
    book = get_object_or_404(Book, id=book_id)
    book.status = 'READING'
    book.save()  # Crucial! This saves the change back to the database.
    return redirect('dashboard')


# 5. QUICK ACTION: COMPLETE READING (Reading -> Completed + Rating)
def complete_reading(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    # Since we need a rating to complete, we read it from the submission form (using POST)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            book.rating = int(rating)
        book.status = 'COMPLETED'
        book.save()

    return redirect('dashboard')
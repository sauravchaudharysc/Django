from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-rating')
    return render(request, 'book_outlet/index.html', {
        'books': books,
        'total_books': books.count(),
        'average_rating': books.aggregate(Avg('rating'))
    })    

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(id=book_id)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)    
    return render(request, 'book_outlet/book_detail.html', {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
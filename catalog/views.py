from django.shortcuts import render
from catalog.models import Book, BookInstance, Genre, Language, Author
from django.views import generic


def index(request):
    """View func for home page"""

    # Generate counts of Book & BookInstance objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Count of available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Count of authors
    num_authors = Author.objects.all().count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {'num_books': num_books, 'num_instances': num_instances,
               'num_instances_available': num_instances_available, 'num_authors': num_authors,
               'num_visits': num_visits, }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class GenreListView(generic.ListView):
    model = Genre


class GenreDetailView(generic.DetailView):
    model = Genre

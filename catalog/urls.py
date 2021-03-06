from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('books/', views.BookListView.as_view(), name='books'),
               path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
               path('authors/', views.AuthorListView.as_view(), name='authors'),
               path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
               path('genres/', views.GenreListView.as_view(), name='genres'),
               path('genres/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail')
               ]

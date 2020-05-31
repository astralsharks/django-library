from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('adaptations/', views.AdaptationListView.as_view(), name='adaptations'),
    path('adaptation/<int:pk>', views.AdaptationDetailView.as_view(), name='adaptation-detail'),
    path('directors/', views.DirectorListView.as_view(), name='directors'),
    path('director/<int:pk>', views.DirectorDetailView.as_view(), name='director-detail'),
]
from django.conf import settings
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('home',home,name='home'),
    path('customer_books',customer_books,name='customer_books'),
    path('book',BookView.as_view(), name='books'),
    path("addbook",BookCreateView.as_view(),name='addbook'),
    path('book-update/<pk>',BookUpdateView.as_view(),name='book-update'),
    path('book-delete/<pk>',BookDeleteView.as_view(),name='book-delete'),
    path('book-detail/<pk>',BookDetailView.as_view(),name='book-detail'),
    
    
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

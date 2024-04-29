from django.urls import path
from . import views

urlpatterns = [
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
]

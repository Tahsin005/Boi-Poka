from django.urls import path
from . import views

urlpatterns = [
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('borrowed_book_list/', views.BorrowedBookView.as_view(), name='borrowed_books'),
    path('borrow_book/<int:pk>', views.borrow_book, name='borrow_book'),
    path('borrowed_book/<int:pk>', views.BookReturnView.as_view(), name='borrowed_book'),
    path('return_book/<int:pk>', views.ReturnBook, name='return_book'),
]

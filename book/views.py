from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, ListView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
from transaction.models import Transaction
from django.contrib.auth.decorators import login_required
from transaction.constants import RETURN, BORROW, DEPOSIT
from review.forms import ReviewForm

# Create your views here.
class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        reviews = book.reviews.all()
        
        context["comments"] = reviews
        context["reviews"] = reviews
        
        return context

@login_required
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    request.user.account.borrowd_books.add(book)
    
    if request.user.account.balance < book.price:
        return  redirect('deposit_money')
    else:
        Transaction.objects.create(
            user = request.user.account,
            amount = book.price,
            balance_after_transaction = request.user.account.balance - book.price,
            transaction_type = BORROW
        )
        
        account = request.user.account
        account.balance -= book.price
        account.save(
            update_fields=[
                'balance'
            ]
        )
        
        return redirect('borrowed_books')

class BorrowedBookView(ListView, LoginRequiredMixin):
    template_name = 'book/borrowed_books.html'
    model = Book
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(
            books=self.request.user.account
        )
        
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['books'] = self.get_queryset()
        
        return context

class BookReturnView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book/book_return.html'
    pk_url_kwarg = 'pk'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        reviews = book.reviews.all()
        review_form = ReviewForm()
        
        context["comments"] = reviews
        context["reviews"] = reviews
        context["review_form"] = review_form
        
        return context

@login_required
def ReturnBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    request.user.account.borrowd_books.remove(book)
    
    Transaction.objects.create(
        user=request.user.account, 
        amount=book.price, 
        balance_after_transaction = request.user.account.balance + book.price, 
        transaction_type=RETURN
    )
    
    account = request.user.account
    account.balance += book.price 
    account.save(
        update_fields=[
            'balance'
        ]
    )
    
    
    return redirect("borrowed_books")
    
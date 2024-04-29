from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book
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


    
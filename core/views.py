from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from book.models import Book, Category

# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['books'] = Book.objects.all()
        context['genres'] = Category.objects.all()
        return context

def home(request, genre):
    genres = Category.objects.all()
    books = Book.objects.filter(genres__name=genre)
    
    return render(request, "core/home.html", {"books":books, "genres":genres})
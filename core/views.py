from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from book.models import Book, Category

# Create your views here.
class HomeView(TemplateView):
    template_name = 'core/home.html'
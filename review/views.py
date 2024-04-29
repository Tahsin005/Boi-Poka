from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from book.models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def review(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            form.save()
        return redirect('home')
    
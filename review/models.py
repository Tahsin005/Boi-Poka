from django.db import models
from book.models import Book
from django.contrib.auth.models import User 
# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    text = models.TextField()
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'Review : {self.text}'

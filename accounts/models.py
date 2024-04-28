from django.db import models
from django.contrib.auth.models import User
from book.models import Book
# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name="account", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    borrowd_books = models.ManyToManyField(Book, related_name='books')
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} : {self.user.first_name} : {self.user.last_name}'
        
    
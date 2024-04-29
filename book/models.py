from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'Language : {self.name}'
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'Category : {self.name}'

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="myimage")
    first_published = models.DateField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True, null=True)
    genres = models.ManyToManyField(Category, related_name='genres')
    
    def __str__(self) -> str:
        return f'Title : {self.title}'
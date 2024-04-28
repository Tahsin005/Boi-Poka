from django.contrib import admin
from . models import Book, Language, Category
# Register your models here.
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Category)
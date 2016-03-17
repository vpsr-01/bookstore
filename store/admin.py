from django.contrib import admin

# Register your models here.
from .models import Book, Author



class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')

class AuthorAdmin(admin.ModelAdmin):
    list_display= ('last_name', 'first_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)


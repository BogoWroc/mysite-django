from django.contrib import admin

from .models import Author, Book, Publisher


# Customize authors list at admin page - replace single columnt(default __str__) by three columns
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(Publisher)

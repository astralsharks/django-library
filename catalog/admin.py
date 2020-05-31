from django.contrib import admin
from .models import Author, Genre, Book, Director, Adaptation

# Register your models here.
# admin.site.register(Book)

# Register the Admin classes for Book using the decorator
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year')

# admin.site.register(Author)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Director, DirectorAdmin)

@admin.register(Adaptation)

class AdaptationAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year')

# admin.site.register(BookInstance)
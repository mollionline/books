from django.contrib import admin
from .models import Book, Review, Genre


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover', 'description', 'created_at', 'updated_at', 'genre')
    list_filter = ('author',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'updated_at')
    list_filter = ('author',)

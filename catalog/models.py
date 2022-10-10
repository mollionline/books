from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class AbstractDate(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения", blank=True)

    class Meta:
        abstract = True


class Book(AbstractDate):
    name = models.CharField(verbose_name='Название книги', max_length=50)
    author = models.ManyToManyField(get_user_model(), related_name='book_author')
    cover = models.ImageField(null=True, blank=True, upload_to='cover_pics', verbose_name='Обложка')
    description = models.TextField(verbose_name='Описание', max_length=150, null=True, blank=True)
    genre = models.ForeignKey('catalog.Genre', related_name='book_genre', on_delete=models.CASCADE)
    review = models.ManyToManyField('catalog.Review', related_name='book_review')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=100)

    def __str__(self):
        return self.name


class Review(AbstractDate):
    rating = models.PositiveIntegerField()
    author = models.ForeignKey(get_user_model(), related_name='review_author', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Отзыв', max_length=250, null=True, blank=True)

    def __str__(self):
        return self.text[:10]

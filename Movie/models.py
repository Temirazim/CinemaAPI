from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class MovieShots(models.Model):
    title = models.CharField(max_length=255, verbose_name='Кадры фильма', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Кадр из фильма'
        verbose_name_plural = 'Кадры фильма'


class Feedback(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255, verbose_name='Автор отзыва', blank=True)
    text = models.TextField(verbose_name='Отзыв', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class StarsRating(models.Model):
    stars_rating = models.IntegerField(verbose_name='Рейтинг актёра', blank=True)

    def __str__(self):
        return str(self.stars_rating)

    class Meta:
        ordering = ['stars_rating']
        verbose_name = 'Рейтинг актёра'
        verbose_name_plural = 'Рейтинг актёров'


class Actors(models.Model):
    name = models.CharField(max_length=255, verbose_name='Актёр', blank=True)
    age = models.IntegerField(verbose_name='Возраст', blank=True)
    description = models.TextField(verbose_name='Биография', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    stars_rating = models.ForeignKey(StarsRating, on_delete=models.CASCADE, verbose_name='Рейтинг актёра', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Актрёр'
        verbose_name_plural = 'Актёры'


class Rating(models.Model):
    stars = models.IntegerField(verbose_name='Рейтинг фильма', blank=True)

    def str(self):
        return self.stars

    class Meta:
        ordering = ['stars']
        verbose_name = 'Рейтинг фильма'
        verbose_name_plural = 'Рейтинг фильмов'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория', blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Genre(models.Model):
    title = models.CharField(max_length=255, verbose_name='Жанр', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Staff(models.Model):
    name = models.CharField(max_length=255, verbose_name='Режисёр', blank=True)
    age = models.IntegerField(verbose_name='Возраст', blank=True)
    description = models.TextField(verbose_name='Биография', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Коллектив'
        verbose_name_plural = 'Коллектив'


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True)
    slogan = models.CharField(max_length=255, verbose_name='Слоган', blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Постер')
    year = models.DateField(verbose_name='Год выпуска', blank=True)
    country = models.CharField(max_length=255, verbose_name='Страна создания', blank=True)
    staff = models.ForeignKey(Staff, on_delete=CASCADE, verbose_name='Коллектив', blank=True)
    actors = models.ForeignKey(Actors, on_delete=CASCADE, verbose_name='Актеры', blank=True)
    genre = models.ForeignKey(Genre, on_delete=CASCADE, verbose_name='Жанры', blank=True)
    world_premiere = models.CharField(max_length=255, verbose_name='Примеьра в мире', blank=True)
    budget = models.CharField(max_length=255, verbose_name='Бюджет', blank=True)
    fees_USA = models.CharField(max_length=255, verbose_name='Сборы в сша', blank=True)
    fees_world = models.CharField(max_length=255, verbose_name='Сборы в мире', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', blank=True)
    slug = models.SlugField(max_length=255, verbose_name='Ссылка', unique=True)
    feedback = models.ForeignKey(Feedback, on_delete=CASCADE, verbose_name='Отзывы', blank=True)
    rating = models.ForeignKey(Rating, on_delete=CASCADE, verbose_name='Рейтинг', blank=True)
    movie_shots = models.ForeignKey(MovieShots, on_delete=CASCADE, verbose_name='Кадры из фильма', blank=True)
    stars_rating = models.ForeignKey(StarsRating, on_delete=CASCADE, verbose_name='Рейтинг звезд', blank=True)
    user = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Пользователь')

    def get_absolute_url(self):
        return reverse('movie', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

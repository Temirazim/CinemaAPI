from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    model = Movie
    save_as = True
    save_on_top = True
    list_display = (
        'id', 'title', 'slug', 'category', 'slogan', 'description', 'actors', 'genre', 'staff', 'rating',
        'stars_rating', 'feedback', 'photo', 'get_photo', 'year', 'country', 'world_premiere',
        'budget', 'fees_USA', 'fees_world', 'movie_shots')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'year')
    readonly_fields = ('get_photo',)
    fields = (
    'title', 'slug', 'category', 'slogan', 'description', 'actors', 'genre', 'staff', 'rating', 'stars_rating',
    'feedback', 'photo', 'get_photo', 'year', 'country',
    'world_premiere', 'budget', 'fees_USA', 'fees_world', 'movie_shots')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'age', 'description', 'stars_rating', 'photo', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    readonly_fields = ('get_photo',)
    fields = ('name', 'age', 'description', 'stars_rating', 'photo', 'get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'name', 'age', 'description', 'photo', 'get_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    fields = ('name', 'age', 'description', 'photo', 'get_photo')
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'photo', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('get_photo',)
    fields = ('title', 'photo', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'stars')
    list_display_links = ('id', 'stars')
    search_fields = ('stars',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'slug', 'title', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


@admin.register(StarsRating)
class StarsRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'stars_rating')
    list_display_links = ('id', 'stars_rating')
    search_fields = ('stars_rating',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'text')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title',)

# Register your models here.
from django.contrib import admin
from .models import Article
from .models import Movie

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    search_fields = ('title', 'author')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')  # Customize the columns displayed in the admin list
    search_fields = ('title',)               # Add a search box for the movie titles

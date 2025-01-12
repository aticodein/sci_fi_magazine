# Create your views here.

from django.shortcuts import render
from .models import Article, Movie
from django.shortcuts import render, get_object_or_404


def home(request):
    articles = Article.objects.all().order_by('-publish_date')[:5]  # Fetch latest 5 articles
    movies = Movie.objects.all().order_by('-release_date')  # Fetch all movies (no limit)
    return render(request, 'home.html', {'articles': articles, 'movies': movies})

def react_home(request):
    return render(request, "index.html")  # Match the correct file path

def article_detail(request, article_id):
    """
    Display the full article.
    """
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})

# Suggest improvements for this function

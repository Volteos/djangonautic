from django.shortcuts import render
from .models import Article

def articlesList(request):
	articles = Article.objects.all().order_by('title')
	return render(request, 'articles/articles.html', {'articles':articles})
# from urllib import request
from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def read(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/read.html', context)


def create(request):
    return render(request, 'articles/create.html')

def post(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:read')
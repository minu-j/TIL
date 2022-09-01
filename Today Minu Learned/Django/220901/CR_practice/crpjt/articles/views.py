from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    email = request.GET.get('email')
    content = request.GET.get('content')
    article = Article(title=email, context=content)
    article.save()
    return redirect('articles:index')


from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe, require_GET
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        form = ArticleForm
    context = {
        'form': form,
    }
    return render(request, "articles/create.html", context)

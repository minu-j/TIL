from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):

    # DB의 전체 데이터를 조회
    articles = Article.objects.all()
    return render(request, 'articles/index.html')
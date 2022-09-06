CRUD/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

CRUD/base.html

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</head>
<body>
    {% block content %}
    {% endblock content %}
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
</body>
</html>
```

articles/forms.py

```python
from turtle import textinput
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력해주세요',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력해주세요',
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
```

articles/models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

articles/urls.py

```python
from . import views

app_name= 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]

```

articles/views.py

```python
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

articles/template/index.html

```django
{% extends 'base.html' %}

{% block content %}

<h1>INDEX</h1>
<hr>
<a href="{% url 'articles:create' %}">CREATE</a>
{% for article in articles %}
    <h3>title: {{ article.title }}</h3>
    <p>content: {{ article.content }}</p>
    <p>created: {{ article.created_at }}</p>
    <p>updated: {{ article.updated_at }}</p>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
{% endfor %}

{% endblock content %}
```

articles/template/create.html

```django
{% extends 'base.html' %}

{% block content %}

<h1>CREATE</h1>
<hr>
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
<a href="{% url 'articles:index' %}">BACK</a>

{% endblock content %}
```

articles/template/detail.html

```django
{% extends 'base.html' %}

{% block content %}

<h1>DETAIL</h1>
<hr>
<p>number: {{ article.pk }}</p>
<h3>title: {{ article.title }}</h3>
<p>content: {{ article.content }}</p>
<p>created: {{ article.created_at }}</p>
<p>updated: {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:update' article.pk %}">EDIT</a>
<form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
<a href="{% url 'articles:index' %}">BACK</a>

{% endblock content %}
```

articles/template/update.html

```django
{% extends 'base.html' %}

{% block content %}

<h1>UPDATE</h1>
<hr>
<form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
</form>
<a href="{% url 'articles:index' %}">BACK</a>

{% endblock content %}
```


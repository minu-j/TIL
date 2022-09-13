### Django 설치

`$ pip install django==3.2.13`

### 가상환경 생성

`$ python -m venv venv`



### venv환경 실행(실행되면 경로 상단에 (venv) 출력)

`$ source venv/Scripts/activate`



### 현재 있는 가상환경 내에서의 패키지 목록 생성

`$ pip freeze > requirements.txt`



### 패키지 목록 설치

`$ pip install -r requirements.txt`



### 패키지 목록 내역 출력

`$ pip list`



### django project 생성

`$ django-admin startproject firstpjt .`



### server 실행

`$ python manage.py runserver`



### app 생성 및 등록

1. app 생성 `$ python manage.py startapp articles`

2. 등록
   
   ```python
   # Application definition
   
   INSTALLED_APPS = [
       'articles',
   ```



### 모든 페이지에 동일한 내용 출력하기

```python
# settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
...
```

```django
# index.html

{% extends 'base.html' %}

{% block content %}

<h1>제목</h1>

{% endblock content %}

===================

# base.html

<body>
  {% block content %}
    # index.html의 내용이 삽입됨
  {% endblock content %}
</body>
```


## Template namespace


### url namespace 지정

urls.py

app_name = 'appname'

url name 지정 후 'appname:index'


### Template namespace 지정

appname/template/appname/index.html 형태로 경로를 지정

  django는 template/ 뒤부터 경로를 읽기 때문


### User Model 대체하기

1. accounts/models.py

  ```python
  from django.contrib.auth.models import AbstractUser

  # Create your models here.
  class User(AbstractUser):
      pass
  ```

2. settings.py

  ```python
  AUTH_USER_MODEL = 'accounts.User'
  ```

3. accounts/admin.py

  ```python
  from django.contrib.auth.admin import UserAdmin
  from .models import User

  # Register your models here.
  admin.site.register(User, UserAdmin)
  ```

## DB Migrations

models.py에 변경사항 발생시 DB에 동기화 하는 작업


### 마이그레이션 생성

`$ python manage.py makemigrations`


### DB에 migrate

`$ python manage.py migrate`


### database 초기화

1. migrations파일 삭제(번호가 붙은 파일만 삭제)

2. db.sqlite3 삭제

3. migrations 진행


## CRUD


### ModelForm 선언

articles/forms.py
```python
from dataclasses import fields
from django import forms
from .models import Articles

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Articles
        fields = '__all__'
```

### Allowed HTTP decorator

```python
from django.views.decorators.http import require_http_methods, require_POST, require_safe

@require_http_methods(['GET', 'POST'])

@require_POST

@require_safe
```


### CREATE

```python
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

### READ

```python
@require_safe
def detail(request, pk):
    article = Articles.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

### UPDATE

```python
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == "POST":
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
```

### DELETE

```python
# 데코레이터 사용(POST요청 외 접근 불가)
@require_POST
def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# if문 사용
def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

## Authentication
```python
from django.contrib.auth.forms import AuthenticationForm
```

### LOGIN

```python
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```
### LOGIN
```python
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

## User CRUD

### UserCreationForm, UserChangeForm 커스텀

accounts/forms.py
  ```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationFrom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)   # 회원가입시 추가적인 정보 수집


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)   # 회원정보수정 출력 내용 제한
  ```

### SIGNUP

```python
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   
            auth_login(request, user)   # 회원가입 후 곧바로 로그인 진행
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```


### DELETE

```python
def delete(request):
    request.user.delete()
    auth_logout(request)   # 탈퇴 후 세션 삭제
    return redirect('articles:index')
```

### UPDATE

```python
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```

### Change Password

```python
from django.contrib.auth.forms import PasswordChangeForm

# 비밀번호 변경시 세션 유지하기
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)   # 비밀번호 변경시 세션 유지하기
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```


### 로그인, 비로그인 상태 출력을 다르게 하기 

```django
{% if request.user.is_authenticated %}
<!-- 로그인 상태에서만 표시될 것들 -->
{% else %}
<!-- 비로그인 상태에서만 표시될 것들 -->
{% endif %}
```
$ pip install django==3.2.13

### 가상환경 생성하기

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


## DB Migrations

models.py에 변경사항 발생시 DB에 동기화 하는 작업


### 마이그레이션 생성

`$ python manage.py makemigrations`


### DB에 migrate

`$ python manage.py migrate`


## ORM
객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술

### 사전준비 : Django shell

설치

`$ pip install ipython`

`$ pip install django-extensions`

실행

`python manage.py shell_plus`

```python
In [1]: Article.objects.all()
Out[1]: <QuerySet []>
```

### QuerySet API

database API 구문

`{Modeclass}.{Manager}.{QuerysetAPI}`

QuerySet : 데이터베이스에게서 전달 받은 객체 목록(데이터의 모음)

CRUD (Create / Read / Update / Delete) : 
대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지

### 데이터 객체를 생성하는 3가지 방법

1. article = Article()
2. article.title
3. article.save()
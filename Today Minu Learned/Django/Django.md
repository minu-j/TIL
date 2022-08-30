$ pip install django==3.2.13



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

1. app 생성 ```$ python manage.py startapp articles```

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

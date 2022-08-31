### 1. Model 반영하기
“Django가 Model에 생긴 변화를 DB에 반영하는 방법” 을 뜻하는 용어를 작성하시오.

**마이그레이션**


### 2. Model 변경사항 저장하기
```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```

1. 위에서 작성한 Model의 변경사항을 저장하기 위한 명령어를 작성하시오.

    `$ python manage.py makemigrations`

2. 이로 인해 생성된 마이그레이션 파일에 대응되는 SQL문을 확인하기 위한 명령어와
출력결과를 작성하시오. (app의 이름은 articles이다.)

    `$ Article.objects.all()`


### 3. Python Shell
Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때,
어떤 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.

$ python manage.py shell_plus


### 4. Django Model Field
Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성하시오.

1. int()
2. text()
3. DataField()
4. CharField()
5. TextField()
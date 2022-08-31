from django.db import models

# Create your models here.
class Article(models.Model):
    # 타입 클래스를 불러와서 인스턴스(필드 이름 스키마)를 생성
    title = models.CharField(max_length=10)   # CharField = 길이 제한이 있는 텍스트, 길이를 꼭 제한해줘야 함.
    content = models.TextField()   # TextField = 길이가 긴 텍스트
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
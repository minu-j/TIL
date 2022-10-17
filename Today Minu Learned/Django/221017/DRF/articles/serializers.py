from dataclasses import field
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('article',)   # 읽기전용필드로 작성


class ArticleSerializer(serializers.ModelSerializer):
    # 게시글 역참조 댓글 조회
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)   # 댓글 목록
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)   # 댓글 갯수(문자열로 ORM명령어 작성)

    class Meta:
        model = Article
        fields = ('__all__')
        # 특정 필드를 override 혹은 추가한 경우 read_only_fields가 동작하지 않음.
from django.shortcuts import get_list_or_404, get_object_or_404
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':     # 전체 글 리스트 읽기
        # articles = Article.objects.all()   # 글이 없을 경우 빈 쿼리셋 반환
        articles = get_list_or_404(Article)   # 글이 없을 경우 404 응답
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':      # 글 작성
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)   # 게시글이 없을 때 예외로 500 응답
    article = get_object_or_404(Article, pk=article_pk)   # shortcut을 활용하여 게시글이 없을 때 예외로 404 응답

    if request.method == 'GET':     # 단일 글 읽기
        serializers = ArticleSerializer(article)
        return Response(serializers.data)

    elif request.method == 'DELETE':   # 글 삭제
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':   # 글 수정
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':   # 전체 댓글 읽기
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializers = CommentSerializer(comments, many=True)
        return Response(serializers.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':   # 단일 댓글 읽기
        serializers = CommentSerializer(comment)
        return Response(serializers.data)

    elif request.method == 'DELETE':   # 댓글 삭제
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request, article_pk):   # 댓글 작성
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

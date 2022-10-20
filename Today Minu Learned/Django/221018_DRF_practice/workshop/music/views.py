from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializer import ArtistListSerializer, ArtistSerializer, MusicListSerializer, MusicSerializer
from .models import Artist, Music


# Create your views here.
@api_view(['GET', 'POST', ])
def artist_list(request):
    if request.method == 'GET':
        artists = get_list_or_404(Artist)
        serializers = ArtistListSerializer(artists, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):   # valid False : 400 bad request
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', ])
def artist_detail(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(serializer.data)


@api_view(['POST', ])
def music_create(request, artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', ])
def music_list(requset):
    music = get_list_or_404(Music)
    serializers = MusicListSerializer(music, many=True)
    return Response(serializers.data)


@api_view(['GET', 'PUT', 'DELETE', ])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name', )


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('__all__')


class ActorNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name', )


class MovieNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', )


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('__all__')


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieNameSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('__all__')


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorListSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only = True)

    class Meta:
        model = Movie
        fields = ('__all__')


class ActorSerializer(serializers.ModelSerializer):
    movie_set = MovieNameSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('__all__')
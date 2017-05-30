from django.contrib.auth.models import User
from rest_framework import serializers
from movies.models import Movie, Genre

# Movie Serializer
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    genre = serializers.ReadOnlyField(source='genre.name')

    class Meta:
        model = Movie
        fields = ('url', 'id', 'title', 'year', 'genre')

# Genre Serializer
class GenreSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)

    class Meta:
        model = Genre
        fields = ('url', 'id', 'name', 'movies')

# User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username')

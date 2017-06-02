from rest_framework import serializers
from django.contrib.auth.models import User
from movies.models import Movie, Genre

# User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username')


# Genre Serializer
class GenreSerializer(serializers.HyperlinkedModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='movie-detail', read_only=True)
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ('id', 'name', 'url', 'movies_count', 'movies')

    # Counting movies under this genre
    def get_movies_count(self, obj):
        return obj.movies.count()

    # Overriding the update method
    def update(self, instance, validated_data):
        # Update the genre instance
        instance.name = validated_data['name']
        instance.save()
        # Output
        return instance

# Movie Serializer
class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ('url', 'id', 'title', 'year', 'genre')

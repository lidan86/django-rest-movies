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
    # movies = serializers.ReadOnlyField(read_only=True, source='movie.name')
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
    # genre = serializers.ReadOnlyField(source='genre.name')
    # genre = serializers.IntegerField(max_value=None, min_value=0, required=True, read_only=False)
    # genre = GenreSerializer(required=True, read_only=False)

    class Meta:
        model = Movie
        fields = ('url', 'id', 'title', 'year', 'genre')

    # # Overriding the create method
    # def create(self, validated_data):
    #     genre_data = validated_data.pop('genre', None)
    #     if genre_data:
    #         genre = Genre.objects.get_or_create(**genre_data)[0]
    #         validated_data['genre'] = genre
    #     return Movie.objects.create(**validated_data)
    #
    # # Overriding the update method
    # def update(self, instance, validated_data):
    #     # Update the movie instance
    #     instance.title = validated_data['title']
    #     instance.year = validated_data['year']
    #     instance.save()
    #     # Update the genre field
    #     genre_data = validated_data.pop('genre', None)
    #     if genre_data:
    #         genre = Genre.objects.get_or_create(**genre_data)[0]
    #         validated_data['genre'] = genre
    #     return Movie.objects.create(**validated_data)
    #     # Output
    #     return instance

from django.contrib.auth.models import User
from rest_framework import serializers
from movies.models import Movie

class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ('url', 'id', 'title', 'year', 'genre')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username')

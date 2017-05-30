from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from movies.models import Movie, Genre
from movies.serializers import MovieSerializer, UserSerializer, GenreSerializer
from tablib import Dataset

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def simple_upload(request):
    if request.method == 'POST':
        movie_resource = MovieResource()
        dataset = Dataset()
        new_movies = request.FILES['myfile']

        imported_data = dataset.load(new_movies.read())
        result = movie_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            movie_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')

import unittest
from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory, APIClient, RequestsClient
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from movies.models import Movie, Genre
from movies.serializers import MovieSerializer, UserSerializer, GenreSerializer

# Testing the User Model
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="Maikel", password="password123")

    def test_user_exist(self):
        mike = User.objects.get(username="Maikel")
        self.assertEqual(mike.username, 'Maikel')

# Testing the Genre Model
class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(name="Cartoon")
        Genre.objects.create(name="Drama")

    def test_genres_exist(self):
        cartoon = Genre.objects.get(name="Cartoon")
        drama = Genre.objects.get(name="Drama")
        self.assertEqual(cartoon.name, 'Cartoon')
        self.assertEqual(drama.name, 'Drama')

# Testing the Movie Model
class MovieTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(name="History")
        history = Genre.objects.get(name="History")
        Movie.objects.create(title="WWI", year=2000, genre=history)
        Movie.objects.create(title="WWII", year=2001, genre=history)

    def test_movies_exist(self):
        history = Genre.objects.get(name="History")
        wwi = Movie.objects.get(title="WWI")
        self.assertEqual(wwi.title, "WWI")
        self.assertEqual(wwi.year, 2000)
        self.assertEqual(wwi.genre, history)
        wwii = Movie.objects.get(title="WWII")
        self.assertEqual(wwii.title, "WWII")
        self.assertEqual(wwii.year, 2001)
        self.assertEqual(wwii.genre, history)

# Testing the views
class ViewsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    #Users Views
    def test_users_index(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_users_detail_with_no_content(self):
        response = self.client.get('/users/2/')
        self.assertEqual(response.status_code, 404)

    def test_users_detail_with_content(self):
        User.objects.create(username="Maikel", password="password123")
        response = self.client.get('/users/1/')
        self.assertEqual(response.status_code, 200)

    #Genres Views
    def test_genres_index(self):
        response = self.client.get('/genres/')
        self.assertEqual(response.status_code, 200)

    def test_genres_detail_with_no_content(self):
        response = self.client.get('/genres/2/')
        self.assertEqual(response.status_code, 404)

    def test_genres_detail(self):
        Genre.objects.create(name="Cartoon")
        response = self.client.get('/genres/1/')
        self.assertEqual(response.status_code, 200)

    #Movies Views
    def test_movies_index(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)

    def test_movies_detail_with_no_content(self):
        response = self.client.get('/movies/2/')
        self.assertEqual(response.status_code, 404)

    def test_movies_detail(self):
        Genre.objects.create(name="History")
        history = Genre.objects.get(name="History")
        Movie.objects.create(title="WWI", year=2000, genre=history)
        response = self.client.get('/movies/1/')
        self.assertEqual(response.status_code, 200)

# Testing JSON output
class JSONTests(TestCase):
    #GET Requests
    def test_get_users(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'count': 0, 'next': None, 'previous': None, 'results': []})

    def test_get_user(self):
        User.objects.create(username="Maikel", password="password123")
        response = self.client.get('/users/1/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'url': 'http://testserver/users/1/', 'id': 1, 'username': 'Maikel'})

    def test_get_genres(self):
        response = self.client.get('/genres/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'count': 0, 'next': None, 'previous': None, 'results': []})

    def test_get_genre(self):
        Genre.objects.create(name="War")
        response = self.client.get('/genres/1/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'id': 1, 'movies': [], 'movies_count': 0, 'name': 'War', 'url': 'http://testserver/genres/1/'})

    def test_get_movies(self):
        response = self.client.get('/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'count': 0, 'next': None, 'previous': None, 'results': []})

    def test_get_movie(self):
        Genre.objects.create(name="History")
        history = Genre.objects.get(name="History")
        Movie.objects.create(title="WWI", year=2000, genre=history)
        response = self.client.get('/movies/1/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'genre': 'http://testserver/genres/1/', 'id': 1, 'title': 'WWI', 'url': 'http://testserver/movies/1/', 'year': 2000})

    #POST Requests
    def test_add_empty_genre(self):
        response = self.client.post('/genres/')
        self.assertEqual(response.status_code, 403)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'detail': 'Authentication credentials were not provided.'})

    def test_add_genre_without_authentication(self):
        response = self.client.post('/genres/', name='Cartoon')
        self.assertEqual(response.status_code, 403)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'detail': 'Authentication credentials were not provided.'})

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

    # def test_genres_detail_with_no_name(self):
    #     Genre.objects.create()
    #     response = self.client.get('/genres/1/')
    #     self.assertEqual(response.status_code, 404)

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

    # def test_movies_detail_with_no_title(self):
    #     Genre.objects.create(name="Fiction")
    #     fiction = Genre.objects.get(name="Fiction")
    #     Movie.objects.create(year=2000, genre=fiction)
    #     response = self.client.get('/movies/1/')
    #     self.assertEqual(response.content, 200)
    #     self.assertEqual(response.status_code, 404)

# Testing JSON output
class AddItemToCollectionTest(TestCase):

    def test_add_empty_genre(self):
        response = self.client.post('/genres/')
        self.assertEqual(response.status_code, 403)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'detail': 'Authentication credentials were not provided.'})

    def test_add_genre_without_authentication(self):
        response = self.client.post('/genres/', name='Cartoon')
        self.assertEqual(response.status_code, 403)
        self.assertJSONEqual(str(response.content, encoding='utf8'),{'detail': 'Authentication credentials were not provided.'})

    # def test_add_genre_with_name_and_authentication(self):
        # User.objects.create(username="Maikel", password="password123")
        # maikel = User.objects.get(username="Maikel")
        # client = APIClient()
        # client.force_authenticate(user=maikel)
        # client.login(username='Maikel', password='password123')
        # response = self.client.post('/genres/', {'name': 'Cartoon'}, format='json')
        # self.assertEqual(response.status_code, 200)
        # factory = APIRequestFactory()
        # request = factory.post('/genres/', {'name': 'Cartoon'})
        # response = client.get('http://localhost:8000/genres/1/')
        # response = factory.post('/genres/', {'name': 'Cartoon'})
        # self.assertJSONEqual(str(response.content, encoding='utf8'),{'status': 'success'})







    # def test_add_genre(self):
    #     response = self.client.post('/genres/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertJSONEqual(
    #         str(response.content, encoding='utf8'),
    #         {'status': 'success'}
    #     )

    # Genre.objects.create(name="Cartoon")
    # self.assertJSONEqual(str(response.content, encoding='utf8'),{'name': 'success'})
    #
    # self.assertEqual(len(mail.outbox), 1)
    # self.assertEqual(len(response.content), 1)

    # Using the standard RequestFactory API to create a form POST request
    # factory = APIRequestFactory()
    # request = factory.post('/genres/', {'name': 'Cartoon'})
    # request = factory.put('/genres/1/', {'name': 'Fiction'})
    # request = factory.delete('/genres/1/')

    # client = RequestsClient()
    # response = client.get('http://localhost:8000/users/')
    # assert response.status_code == 200

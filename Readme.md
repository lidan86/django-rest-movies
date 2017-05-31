# Django REST Framework - Movies & Genres

# Project Description
- This is an API for movies and genres. I made it as a part of a code challenge for Mariana Tek.
- The API supports full CRUD (create, read, edit, and delete) functionality for both movies and genres.
- The API is read-only for un-authenticated users. Only authenticated users have access to the full CRUD functionality. There is currently one user authorized to manipulate data on this API. The user name is 'admin', and the password is 'password123'
- The API provides data in two formats: JSON and HTML.
- Data in the API was provided as a tsv file by Mariana Tek. It was imported to the SQLite database by using the 'import_export' package.
- The API allows filtering movies by genre. Each genre has a count of movies produced under this genre, and a list of links to these movies instances.

# Instructions
1. To start the API
Open your terminal
$ cd movies                     # Browse into the repo root directory
$ source env/bin/activate       # Launch the environment
$ cd cinema                     # Browse into the project directory
$ python manage.py runserver    # Start the server
2. To be able to make API calls through the terminal
$ sudo easy_install pip         # instals Pip package manager
$ pip install httpie            # instals HTTPie package
3. For API SCHEMA
Browser: http://localhost:8000/schema/
CLI: $ http http://localhost:8000/schema/
4. For a list of all users
Browser: http://localhost:8000/users/
CLI: $ http http://localhost:8000/users/
5. For a list of all movies
Browser: http://localhost:8000/movies/
CLI: $ http http://localhost:8000/movies/
6. For a particular movie
Browser: http://localhost:8000/movies/:id/
CLI: $ http http://localhost:8000/movies/:id/
7. For a list of all genres
Browser: http://localhost:8000/genres/
CLI: $ http http://localhost:8000/genres/
8. For a particular genre
Browser: http://localhost:8000/genres/:id/
CLI: $ http http://localhost:8000/genres/:id/
9. API post requests
CLI: $ http -a user:password POST http://127.0.0.1:8000/movies/ title='title' year='year' genre='genre'
CLI: $ http -a user:password POST http://127.0.0.1:8000/genres/ name='name
* Don't forget to replace the username and password!
* If you post a movie with a genre which doesn't exist, the new genre will be created.
* Genre names are case sensitive. 'History' is different than 'history.'
10. API Put requests
CLI: $ http -a user:password Put http://127.0.0.1:8000/movies/ title='title' year='year' genre='genre'
CLI: $ http -a user:password PUT http://127.0.0.1:8000/genres/:id/ name='new_name'
11. API delete requests
CLI: $ http -a user:password DELETE http://localhost:8000/movies/:id/
CLI: $ http -a user:password DELETE http://127.0.0.1:8000/genres/:id/
* if you delete a genre, all movies under this genre will be deleted.
12. Access the admin website
Browser: http://localhost:8000/admin/

# Tasks:
1. Load the `movies_genres.tsv` into the Django using a SQLite database. - DONE
2. Create a JSON REST API  - A web api client should be able to create, retrieve, list, update, and delete movies and genres - DONE
3. A web api client should be able to filter movies by genre - DONE
4. A web api client should be able to retrieve and list counts of movies by genre - DONE

5. A web api client should be able to retrieve or list which genre had the most movies per year.  The returned data should include the year, genre name, and count.
6. A web api client should be able to retrieve or list movies that include a "number of sequels" field based on whether this movie name is a prefix of other movies.  For example, "The Godfather" is a prefix of "The Godfather Part II" and "The Godfather Part III", so the REST endpoint for "The Godfather" should show a sequel count of 2.  Note, you can add this to the existing "movies" REST API from the core API you wrote above.

7. Write tests for your code
8. Document as needed. - Done

# Issues
- API movie post and put requests errors because of the nested resource.
- Duplication is currently allowed. You can have several genres with the same name. Then, if you want to add a movie to any of them, it will error.
- Genre detail shows a list of movies urls, not movies name.
- In the terminal, the genre object appears before the other fields in the movie instance.

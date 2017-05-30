# Django REST Framework - Movies & Genres

# Project Description
- This is an API for movies and genres. I made it as a part of a code challenge for Mariana Tek.
- The API supports full CRUD (create, read, edit, and delete) functionality for both movies and genres.
- The API is read-only for un-authenticated users. Only authenticated users have access to the full CRUD functionality.
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

# Tasks:
1. Load the `movies_genres.tsv` into the Django using a SQLite database. - DONE
2. Create a JSON REST API  - A web api client should be able to create, retrieve, list, update, and delete movies and genres - DONE
3. A web api client should be able to filter movies by genre - DONE
4. A web api client should be able to retrieve and list counts of movies by genre - DONE

5. A web api client should be able to retrieve or list which genre had the most movies per year.  The returned data should include the year, genre name, and count.
6. A web api client should be able to retrieve or list movies that include a "number of sequels" field based on whether this movie name is a prefix of other movies.  For example, "The Godfather" is a prefix of "The Godfather Part II" and "The Godfather Part III", so the REST endpoint for "The Godfather" should show a sequel count of 2.  Note, you can add this to the existing "movies" REST API from the core API you wrote above.

7. Write tests for your code
8. Document as needed.  

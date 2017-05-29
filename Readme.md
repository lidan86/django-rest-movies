# Tasks:

1. Load the `movies_genres.tsv` into the Django using a SQLite database. - DONE
2. Create a JSON REST API  - A web api client should be able to create, retrieve, list, update, and delete movies and genres

3. A web api client should be able to filter movies by genre
4. A web api client should be able to retrieve and list counts of movies by genre
5. A web api client should be able to retrieve or list which genre had the most movies per year.  The returned data should include the year, genre name, and count.

6. A web api client should be able to retrieve or list movies that include a "number of sequels" field based on whether this movie name is a prefix of other movies.  For example, "The Godfather" is a prefix of "The Godfather Part II" and "The Godfather Part III", so the REST endpoint for "The Godfather" should show a sequel count of 2.  Note, you can add this to the existing "movies" REST API from the core API you wrote above.

7. Write tests for your code
8. Document as needed.  

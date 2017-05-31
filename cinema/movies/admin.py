from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Movie, Genre

# Giving the admin website access to the Genre model
@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    pass

# Giving the admin website access to the Movie model
@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    pass

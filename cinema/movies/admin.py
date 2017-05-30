from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Movie, Genre

@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    pass

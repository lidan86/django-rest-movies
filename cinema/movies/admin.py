from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    pass

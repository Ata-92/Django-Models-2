from django.contrib import admin

from dj_relationships.models import Creator, Language

# Register your models here.
admin.site.register(Creator, Language)

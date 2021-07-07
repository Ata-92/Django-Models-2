from django.contrib import admin

from dj_relationships.models import Creator, Framework, Language, Programmer

# Register your models here.
admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Programmer)

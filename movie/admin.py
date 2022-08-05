from django.contrib import admin
from .models import *

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','genre','release_date','hit','avg_ratings','available_on_otts']


class CastAdmin(admin.ModelAdmin):
    list_display=['movie','actor','gender','movie_Charcter_name']


admin.site.register(Movie,MovieAdmin)
admin.site.register(Cast,CastAdmin)

from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from . models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields=['id','name','genre','release_date','hit','avg_ratings','available_on_otts']

class CastSerializer(serializers.ModelSerializer):
    movie_name=serializers.CharField(source='movie.name')
    
    class Meta:
        model=Cast
        fields=['id','actor','gender','movie_Charcter_name','movie_name']
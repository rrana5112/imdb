from tkinter import CASCADE
from django.db import models


# Create a models 
# 1. Movies (Name, genre,Release date, hit,avg_ratings, available_on_otts : name of all OTTs where available or Null) and, 
# 2. Cast : (Movie, Name, Movie char Name)

class Movie(models.Model):
    name=models.CharField(max_length=1000)
    genre=models.CharField(max_length=50)
    release_date=models.DateField()
    hit=models.BooleanField(default=False)
    avg_ratings=models.FloatField()
    available_on_otts=models.TextField(null=True,blank=True)

    def __unicode__(self):
        return self.name

class Cast(models.Model):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='movie')
    actor=models.CharField(max_length=100)
    gender_choice=(
        ('Male','Male'),
        ('Female', 'Female'),
        ('Other','Other'),
    )
    
    gender=models.CharField(choices=gender_choice,null=False,blank=False,max_length=10)
    movie_Charcter_name=models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

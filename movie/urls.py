from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.Movie_get.as_view()),
    path('movies/<int:pk>/', views.Movie_data.as_view()),
    path('cast/',views.Cast_get.as_view()),
    path('cast/<int:pk>/', views.Cast_data.as_view()),
    path('search_movie/',views.Search_Movie.as_view()),
    path('search_cast/',views.Search_cast.as_view()),
    ]
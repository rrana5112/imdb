from webbrowser import get
from django.shortcuts import redirect, render
from movie.serializer import CastSerializer, MovieSerializer
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework import status

# Create API for getting all Movies
# Create API for adding Movie Details
# Create API for updating and deleting Movie data.
# Create API for CRUD APIs for Cast
# Need searching Movies by Name, Actor ,release year and genre
# API for getting cast for a movie.

class Movie_get(APIView):
    def get (self,request):
        movie=Movie.objects.all()
        serializer=MovieSerializer(movie,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Movie Data created'})
        return Response(serializer.errors)



class Movie_data(APIView):
    def get(self,request,pk):
        try:
            if pk is not None:
                movie=Movie.objects.get(id=pk)
                serializer=MovieSerializer(movie)
                return Response(serializer.data)   
            return Response(serializer.errors)
        except Exception as e:
            response = Response({'ERROR':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
            return response
    def put(self,request,pk):
        try:
            if pk is not None:
                movie=Movie.objects.get(id=pk)  
                serializer=MovieSerializer(movie,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'Movie Data updated'})
                return Response(serializer.errors)
        except Exception as e:
            response = Response({'ERROR':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
            return response
    
    def delete(self,request,pk):
        try:
            if pk is not None:
                movie=Movie.objects.get(id=pk)  
                movie.delete()
                return Response({'msg':'Movie Data Deleted'})
        except Exception as e:
            response = Response({'ERROR':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
            return response


class Cast_get(APIView):
    def get(self,request):
        cast=Cast.objects.all()
        serializer=CastSerializer(cast,many=True)
        return Response(serializer.data)
        

    
    def post(self,request):
        serializer=CastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Cast Data created'})
        return Response(serializer.errors)



class Cast_data(APIView):
    def get(self,request,pk):
        try:
            if pk is not None:
                cast=Cast.objects.get(id=pk)    
                serializer=CastSerializer(cast)
                return Response(serializer.data)
            return Response(serializer.errors)
        except Exception as e:
            response = Response({'ERROR':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
            return response

    def put(self,request,pk):
        try:
            if pk is not None:
                cast=Cast.objects.get(id=pk)    
                serializer=CastSerializer(cast,data=request.data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg':'Cast Data updated'})
                return Response(serializer.errors)
        except Exception as e:
            response = Response({'ERROR':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
            return response
       
    def delete(self,request,pk):
        try:
            if pk is not None:    
                cast=Cast.objects.get(id=pk)
                cast.delete()
                return Response({'msg':'Cast Data Deleted'})
        except Exception as e:
            response = Response({'ERROR':status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)
            return response
        

class Search_Movie(ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[SearchFilter]
    search_fields=['^name','release_date','genre']


class Search_cast(ListAPIView):
    queryset=Cast.objects.all()
    serializer_class=CastSerializer
    filter_backends=[SearchFilter] 
    search_fields=['movie']





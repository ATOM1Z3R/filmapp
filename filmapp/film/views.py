from django.http import Http404
from rest_framework.generics import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import *


class UserGetAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self, request):
        try:
            return Film.objects.filter(added_by=request.user)
        except:
            raise Http404

    def get_object(self, pk, request):
        try:
            return Film.objects.get(pk=pk, added_by=request.user)
        except:
            raise Http404

class ListAll(ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmListSerializer

class Detail(APIView):
    def get_object(self, pk):
        try:
            return Film.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        film = self.get_object(pk)
        serializer = FilmDetailSerializer(film)
        return Response(serializer.data)

class UserList(UserGetAPI):
    def get(self, request):
        films = self.get_queryset(request)
        serializer = FilmListSerializer(films, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FilmCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.user, serializer.validated_data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(UserGetAPI):
    def get(self, request, pk):
        film = self.get_object(pk, request)
        serializer = FilmDetailSerializer(film)
        return Response(serializer.data)

    def delete(self, request, pk):
        film = Film.objects.get(pk=pk)
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        film = self.get_object(pk, request)
        serializer = FilmDetailSerializer(film, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Ratings(UserGetAPI):
    def get_queryset(self, request):
        try:
            return Rating.objects.filter(user=request.user)
        except:
            raise Http404
    
    def get(self, request):
        ratings = self.get_queryset(request)
        serializer = RatingReadSerializer(ratings, many=True)
        return Response(serializer.data)

class Rate(UserGetAPI):
    def get_object(self, request, pk):
        try:
            return Rating.objects.get(user=request.user, film__pk=pk)
        except:
            raise Http404

    def post(self, request, pk):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(request.user, pk, serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        rating = self.get_object(request, pk)
        serializer = RatingSerializer(rating, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import *
from django.http import Http404
from rest_framework import status
from .models import *
from .serializers import *


class GetObj(APIView):
    def get_object(self, pk):
        try:
            return Director.objects.get(pk=pk)
        except:
            raise Http404

class ListAll(ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class Create(CreateAPIView):
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated]

class Detail(GetObj):
    def get(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorDetailSerializer(director)
        return Response(serializer.data)

class DetailLogged(GetObj):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorDetailSerializer(director)
        return Response(serializer.data)

    def patch(self, request, pk):
        director = self.get_object(pk)
        serializer = DirectorDetailSerializer(director, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
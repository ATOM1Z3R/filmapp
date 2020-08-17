from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *


class ListAll(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class Detail(RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
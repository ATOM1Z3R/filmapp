from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from register.serializers import RegisterSerializer

class Register(CreateAPIView):
    serializer_class = RegisterSerializer

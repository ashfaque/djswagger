from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q, F
from .models import *
from .serializers import *

from django.shortcuts import render

# Create your views here.


class SwaggerTestCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    queryset = SwaggerTest.objects.all()
    serializer_class = SwaggerTestCreateSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SwaggerTestEditView(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    queryset = SwaggerTest.objects.all()
    serializer_class = SwaggerTestEditSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


class SwaggerTestDeleteView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    queryset = SwaggerTest.objects.all()
    serializer_class = SwaggerTestDeleteSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


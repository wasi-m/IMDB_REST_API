from django.shortcuts import render
from .serializers import dataSerializer
from .models import imdb_data
from rest_framework import generics


# Create your views here.
class dataList(generics.ListCreateAPIView):
    queryset = imdb_data.objects.all()
    serializer_class = dataSerializer

    
class dataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = imdb_data.objects.all()
    serializer_class = dataSerializer

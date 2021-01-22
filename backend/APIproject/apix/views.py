from django.shortcuts import render
from .models import Marks, AnimeList
from .serializer import MarkSerializer, AnimeSerializer
from rest_framework import generics

def home(request):
    return render(request, 'home.html', {})

class listView(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer

class AnimeListView(generics.ListCreateAPIView):
    queryset = AnimeList.objects.all()
    serializer_class = AnimeSerializer


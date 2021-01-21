from django.shortcuts import render
from .models import Marks
from .serializer import MarkSerializer
from rest_framework import generics

def home(request):
    return render(request, 'home.html', {})

class listView(generics.ListCreateAPIView):
    queryset = Marks.objects.all()
    serializer_class = MarkSerializer
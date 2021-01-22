from rest_framework import serializers
from .models import Marks, AnimeList
class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ['name','marks']

class AnimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeList
        fields = '__all__'
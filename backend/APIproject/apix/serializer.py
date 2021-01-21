from rest_framework import serializers
from .models import Marks
class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = ['name','marks']
from rest_framework import serializers
from .models import imdb_data

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = imdb_data
        fields = ('__all__')
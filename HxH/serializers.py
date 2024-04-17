from .models import Personaje
from rest_framework import serializers

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'

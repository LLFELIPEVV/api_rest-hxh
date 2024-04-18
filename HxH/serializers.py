from .models import *
from rest_framework import serializers

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'
    
class CategoriaHabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaHabilidad
        fields = '__all__'

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = '__all__'

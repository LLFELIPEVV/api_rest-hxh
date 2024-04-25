from .models import *
from rest_framework import serializers
    
class CategoriaHabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaHabilidad
        fields = '__all__'

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidad
        fields = ['id', 'nombre', 'descripcion', 'categoria']

class PersonajeSerializer(serializers.ModelSerializer):
    habilidades = HabilidadSerializer(many=True)
    
    class Meta:
        model = Personaje
        fields = ['id', 'nombre', 'tipo', 'habilidades']

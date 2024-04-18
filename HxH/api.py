from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonajeSerializer

class CategoriaHabilidadViewSet(viewsets.ModelViewSet):
    queryset = CategoriaHabilidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategoriaHabilidadSerializer

class HabilidadViewSet(viewsets.ModelViewSet):
    queryset = Habilidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = HabilidadSerializer

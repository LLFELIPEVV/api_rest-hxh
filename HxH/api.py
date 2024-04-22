from .models import *
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
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

"""--- Buscar como unir varios tipos de filtrado ---"""

# Se hereda de PersonajeViewSet para tener la query y CRUD sin tener que duplicar el codigo, y poder filtrar esos resultados
class Filtrado(PersonajeViewSet):
    # Se especifica que se usara SearchFilter como backend de filtrado
    filter_backends = [SearchFilter]
    # Se especifica los campos en los que se permite la busqueda o filtrado
    search_fields = ['nombre', 'tipo']  

class Ordenamiento(PersonajeViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ['nombre', 'tipo', 'habilidades']

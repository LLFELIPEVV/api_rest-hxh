from django.urls import path
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

# Se comenta por que la de Ordenamiento tiene mas funcionalidades y hereda de PersonajeViewSet
#router.register('personajes', PersonajeViewSet, 'personajes')
router.register('personajes', Ordenamiento, 'personajes')
router.register('categoria-habilidad', CategoriaHabilidadViewSet, 'categoria habilidades')
router.register('habilidad', HabilidadViewSet, 'habilidades')
router.register('busqueda_personaje', Filtrado, basename='busqueda_personaje')

urlpatterns = router.urls

from django.urls import path
from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('personajes', PersonajeViewSet, 'personajes')
router.register('categoria-habilidad', CategoriaHabilidadViewSet, 'categoria habilidades')
router.register('habilidad', HabilidadViewSet, 'habilidades')

urlpatterns = router.urls

from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .api import *

router = routers.DefaultRouter()

# Se comenta por que la de Ordenamiento tiene mas funcionalidades y hereda de PersonajeViewSet
#router.register('personajes', PersonajeViewSet, 'personajes')
router.register('personajes', Ordenamiento, 'personajes')
router.register('categoria-habilidad', CategoriaHabilidadViewSet, 'categoria habilidades')
router.register('habilidad', HabilidadViewSet, 'habilidades')
router.register('busqueda_personaje', Filtrado, basename='busqueda_personaje')

urlpatterns = [
    path('docs/', include_docs_urls(title="HxH API"))
]

urlpatterns += router.urls

from rest_framework import viewsets # viewsets, para la creacion de endpoints de API
from .models import BecalImportado
from .serializers import BecalImportadoSerializer


class BecalImportadoViewSet(viewsets.ReadOnlyModelViewSet): # ReadOnlyModelViewSet, solo para leer datos
    queryset = BecalImportado.objects.all() # para obtener los registros de la tabla
    serializer_class = BecalImportadoSerializer # hacemos la conversion a JSON, la clase esta en 'serializers'

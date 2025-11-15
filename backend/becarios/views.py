from rest_framework import viewsets
from .models import BecalImportado
from .serializers import BecalImportadoSerializer

class BecalImportadoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BecalImportado.objects.all()
    serializer_class = BecalImportadoSerializer

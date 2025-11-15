from rest_framework import serializers
from .models import BecalImportado 



class BecalImportadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecalImportado  # Convierte el modelo BecalImportado a formato JSON
        fields = '__all__'  # incluye todos los campos de la tabla.

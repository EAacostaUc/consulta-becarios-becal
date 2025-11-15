from rest_framework import serializers
from .models import BecalImportado


class BecalImportadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BecalImportado
        fields = '__all__'

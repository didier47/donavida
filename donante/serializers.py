from rest_framework import serializers

from donante.models import DonanteModel


class DonanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DonanteModel
        fields = '__all__'

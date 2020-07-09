from rest_framework import serializers

from donor.models import DonorModel


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorModel
        fields = '__all__'

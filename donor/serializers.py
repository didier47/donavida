from django_cassandra.common.utilities import Constants
from rest_framework import serializers

from donor.models import DonorModel


class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorModel
        fields = ['id',
                  'last_login',
                  'email',
                  'password',
                  'first_name',
                  'last_name',
                  'date_joined',
                  'identification',
                  'birth_date',
                  'phone',
                  'address']
        extra_kwargs = {
            'password': {'write_only': True},
            'last_login': {'read_only': True, 'format': Constants.FORMAT_DATE_TIME},
            'date_joined': {'read_only': True, 'format': Constants.FORMAT_DATE_TIME}
        }

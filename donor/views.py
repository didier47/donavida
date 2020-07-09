from rest_framework import viewsets

from donor.models import DonorModel
from donor.serializers import DonorSerializer


class DonorViewSet(viewsets.ModelViewSet):
    queryset = DonorModel.objects.all()
    serializer_class = DonorSerializer

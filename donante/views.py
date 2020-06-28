from rest_framework import viewsets

from donante.models import DonanteModel
from donante.serializers import DonanteSerializer


class DonanteViewSet(viewsets.ModelViewSet):
    queryset = DonanteModel.objects.all()
    serializer_class = DonanteSerializer

from rest_framework import viewsets

from user.models import UserModel
from user.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

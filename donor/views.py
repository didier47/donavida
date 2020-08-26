from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response

from donor.models import DonorModel
from donor.serializers import DonorSerializer
from user.managers import CustomUserManager


class DonorViewSet(viewsets.ModelViewSet):
    queryset = DonorModel.objects.all()
    serializer_class = DonorSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id',
                       'email',
                       'first_name',
                       'last_name',
                       'date_joined',
                       'identification',
                       'birth_date',
                       'phone',
                       'address']
    ordering = ['email']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['email'] = CustomUserManager.normalize_email(serializer.validated_data['email'])
        raw_password = serializer.validated_data.pop('password')
        instance = serializer.save()
        instance.set_password(raw_password)
        instance.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

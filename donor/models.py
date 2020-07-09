from django.db import models

from user.models import UserModel


class DonorModel(UserModel):
    identification = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)

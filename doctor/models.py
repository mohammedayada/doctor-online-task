from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Doctor(User):
    name = models.CharField(max_length=150)
    is_doctor = models.BooleanField(default=True)

    def __str__(self):
        return "doctor name: {}".format(self.username)

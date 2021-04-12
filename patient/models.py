from django.db import models
from django.contrib.auth.models import User
from clinic.models import Clinic

# Create your models here.
class Patient(User):
    name = models.CharField(max_length=150)
    is_patient = models.BooleanField(default=True)

    def __str__(self):
        return "patient name: {}".format(self.username)


class Reservation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    def __str__(self):
        return "patient name: {} clinic name: {}".format(self.patient.username, self.clinic.name)
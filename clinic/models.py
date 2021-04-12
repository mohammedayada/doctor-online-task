from django.db import models
from doctor.models import Doctor


# Create your models here.
class Clinic(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return "clinic name: {} doctor name: {} ".format(self.name, self.doctor.username)

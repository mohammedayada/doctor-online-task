from django.contrib import admin
from .models import Patient, Reservation
# Register your models here.
admin.site.register(Patient)
admin.site.register(Reservation)
from rest_framework import serializers
from .models import Clinic
from django.contrib.auth.hashers import make_password

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ('id', 'name', 'price', 'date', 'start_time', 'end_time', 'doctor')


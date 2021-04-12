from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerClinicOrReadOnly
from django.shortcuts import render
from .models import Clinic
from .serializers import ClinicSerializer


# Create clinic and show all clinics
class ClinicListCreateView(ListCreateAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [IsAuthenticated]


# update and delete specific clinic
class ClinicDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = [IsOwnerClinicOrReadOnly, IsAuthenticated]

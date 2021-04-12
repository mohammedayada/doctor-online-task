from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerDoctorOrReadOnly
from django.shortcuts import render
from .models import Doctor
from .serializers import DoctorSerializer


# Create doctor and show all doctors
class DoctorListCreateView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


# update and delete specific doctor
class DoctorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsOwnerDoctorOrReadOnly, IsAuthenticated]

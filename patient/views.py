from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView, )
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerPatientOrReadOnly, IsOwnerReservationOrReadOnly
from django.shortcuts import render
from .models import Patient, Reservation
from .serializers import PatientSerializer, ReservationSerializer


# Create your views here.
# Display all patients and create new patient
class PatientListCreateView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]


# update or delete patient
class PatientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsOwnerPatientOrReadOnly, IsAuthenticated]


# Display all Reservations and create new pReservation
class ReservationListCreateView(ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


# update or delete Reservation
class ReservationDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsOwnerReservationOrReadOnly, IsAuthenticated]

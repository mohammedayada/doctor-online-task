from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PatientListCreateView, PatientDetailView, ReservationDetailView, ReservationListCreateView

urlpatterns = [
    #gets all Patients and create a new Patient
    path("all", PatientListCreateView.as_view(), name="all-patients"),
    # retrieves Patient of the currently logged in user
    path("details/<int:pk>", PatientDetailView.as_view(), name="patient"),

   #gets all Reservations and create a new reservation
    path("all-reservations", ReservationListCreateView.as_view(), name="all-patients"),
    # retrieves Reservation of the currently logged in user
    path("reservation/<int:pk>", ReservationDetailView.as_view(), name="patient"),
]
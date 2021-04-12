from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClinicListCreateView, ClinicDetailView

urlpatterns = [
    #gets all Doctors and create a new Doctor
    path("all", ClinicListCreateView.as_view(), name="all-clinics"),
   # retrieves doctor of the currently logged in user
    path("details/<int:pk>", ClinicDetailView.as_view(), name="clinic"),
]
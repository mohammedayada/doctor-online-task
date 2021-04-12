from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DoctorListCreateView, DoctorDetailView

urlpatterns = [
    #gets all Doctors and create a new Doctor
    path("all", DoctorListCreateView.as_view(), name="all-doctors"),
   # retrieves doctor of the currently logged in user
    path("details/<int:pk>", DoctorDetailView.as_view(), name="doctor"),
]
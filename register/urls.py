from django.urls import path
from . import views

urlpatterns = [
    path("applicant/", views.get_register_applicant, name= "get_register_applicant"),
    path("employer/", views.get_register_employer, name = "get_register_employer")
]
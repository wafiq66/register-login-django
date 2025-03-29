from django.urls import path
from . import views

urlpatterns = [
    path("applicant/", views.get_login_applicant, name= "get_login_applicant"),
    path("employer/", views.get_login_employer, name="get_login_employer")
]
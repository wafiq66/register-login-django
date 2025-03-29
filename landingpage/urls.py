from django.urls import path
from . import views

app_name = "landingpage"

urlpatterns = [
    path("", views.landing_page, name="landing_page"),
]
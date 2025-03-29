from django.urls import path
from . import views

urlpatterns=[
    path("form/", views.password_reset_form, name="password_reset_form"),
    path("done/", views.password_reset_done, name="password_reset_done"),
    path("confirm/", views.password_reset_confirm, name="password_reset_confirm"),
    path("complete/", views.password_reset_complete, name="password_reset_complete"),
]
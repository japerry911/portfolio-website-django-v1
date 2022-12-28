from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="contact-page"),
    path("success", views.success, name="contact-success-page"),
]

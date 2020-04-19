from django.urls import path

from . import views

urlpatterns = [path("auth", views.Authorise.as_view(), name="twillio-auth")]

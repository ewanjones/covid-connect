from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("register/", views.Register.as_view(), name="register"),
    path("", login_required(views.Home.as_view()), name="home"),
]

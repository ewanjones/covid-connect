from django.contrib.auth import base_user
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, full_name, nickname, phone=None):
        user = self.create(
            email=email, full_name=full_name, nickname=nickname, phone=phone
        )
        user.set_password(password)
        user.save()
        return user


class User(base_user.AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)

    email = models.CharField(unique=True, max_length=100)
    phone = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

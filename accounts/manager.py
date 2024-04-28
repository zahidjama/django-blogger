from . import models
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None):
        if not email:
            raise ValueError("Email Required")
        if not name:
            raise ValueError("Name Required")
        if not phone:
            raise ValueError("Phone Required")


        user=self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, phone, password=None):
        user=self.create_user(
            email=email,
            name=name,
            phone=phone
        )
        user.set_password(password)
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
        
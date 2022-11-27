from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUsermanager(BaseUserManager):

    def createUser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Please provide an email address")
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
            return user

    
    def createSuperuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff to be True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser to be True')
        return self.createUser(email=email, password=password, **extra_fields)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUsermanager

    def __str__(self):
        return self.email


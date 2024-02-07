from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):

        if not email:
            return ValueError("An email field if required!")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

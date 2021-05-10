from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        # if email is an empty string or a None value
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        # hash password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        # password can not be none
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Data model for usera in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # MVC pattern
    object = UserProfileManager()

    # instead of inputting username, users have to input email
    USERNAME_FIELD = 'email'
    # required fields
    REQUIRED_FIELDS = ['name']


    # define a func in a class then have to put self
    def get_full_name(self):
        """Get full name of user"""
        return self.name

    def get_short_name(self):
        """Get short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email

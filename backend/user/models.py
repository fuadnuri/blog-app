from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 

from .managers import CustomerManager

class AdminUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_stuff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email 

        
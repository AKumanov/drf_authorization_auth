from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import uuid

from .managers import CustomUserManager

# Create your models here.
from django.utils import timezone


class Profile(AbstractBaseUser, PermissionsMixin):
    __FIRST_NAME_MAX_LENGTH = 30
    __LAST_NAME_MAX_LENGTH = 50
    # These fields are tied to authorization roles!
    ADMIN = 1
    MANAGER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (EMPLOYEE, 'Employee')
    )

    uid = models.UUIDField(
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='Company identifier'
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=__FIRST_NAME_MAX_LENGTH,
        blank=True
    )
    last_name = models.CharField(
        max_length=__LAST_NAME_MAX_LENGTH,
        blank=True
    )
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default=3
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

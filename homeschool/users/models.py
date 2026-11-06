from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user for extension."""
    pass
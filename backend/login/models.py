from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)

    # Add related_name to resolve the reverse lookup crash
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="user_permissions",
        blank=True,
    )


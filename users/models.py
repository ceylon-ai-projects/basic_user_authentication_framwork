# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add additional fields here. For example, a global-friendly name field
    # name = models.CharField(blank=True, max_length=255)
    # first_name = models.CharField(blank=False, max_length=255)
    # last_name = models.CharField(blank=False, max_length=255)


    def __str__(self):
        return self.email

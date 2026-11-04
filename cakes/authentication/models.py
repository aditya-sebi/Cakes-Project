from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class rolechoices(models.TextChoices):

    ADMIN = 'ADMIN', 'Admin'

    USER = 'USER', 'User'


class Profile(AbstractUser):

    role = models.CharField(max_length=20, choices=rolechoices.choices)

    class Meta:

        verbose_name = 'Profile'

        verbose_name_plural = 'Profiles'

    def __str__(self):

        return self.first_name    



    
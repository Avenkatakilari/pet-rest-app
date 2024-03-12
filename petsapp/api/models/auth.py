from django.db import models

from django.contrib.auth.models import AbstractUser
"""
Author: K V S Aravind 
To store new user into database for authentication purpose
"""

class AppUser(AbstractUser):
  """App user to registrer new user."""

  class Meta:
      db_table = 'appuser'
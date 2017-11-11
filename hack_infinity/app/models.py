from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MyUser(AbstractUser):
	mobile_no = models.CharField(max_length=10, unique=True)



class State_translator(models.Model):
    state_name = models.CharField(max_length=50, default=None)
    state_language = models.CharField(max_length=50, default=None)
    state_code = models.CharField(max_length=20, default="en")

    def __str__(self):
        return self.state_name

    def to_dict(self):
        return convert_to_dict(self)

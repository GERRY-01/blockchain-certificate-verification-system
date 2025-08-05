from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Institution(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    institution_hash = models.CharField(max_length=200)
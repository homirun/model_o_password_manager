from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AccountInformation(models.Model):
    title = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    relation_user_id = models.IntegerField(null=True)



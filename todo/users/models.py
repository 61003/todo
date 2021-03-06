from django.db import models
from uuid import uuid4
from datetime import datetime


class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4())
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    birthdaydate = models.DateTimeField(default=datetime.now())

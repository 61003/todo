from django.db import models
from users.models import User
from datetime import datetime


class Project(models.Model):
   name = models.CharField(max_length=128)
   repo_url = models.CharField(max_length=512)
   users = models.ManyToManyField(User)

   def __str__(self):
       return self.name

class ToDo(models.Model):
    project = models.ForeignKey(Project, models.PROTECT)
    text = models.CharField(max_length=1024)
    create_date = models.DateField(default=datetime.now())
    update_date = models.DateField(default=datetime.now())
    user = models.ForeignKey(User, models.PROTECT)
    is_active = models.BooleanField()
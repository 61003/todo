from rest_framework import serializers
from .models import Project, ToDo
from users.serializers import UserModelSerializer

class ProjectSerializer(serializers.ModelSerializer):
   users = UserModelSerializer(many=True)

   class Meta:
       model = Project
       fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):

   class Meta:
       model = ToDo
       fields = '__all__'


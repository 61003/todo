import graphene
from graphene_django import DjangoObjectType
from users.models import User
from work.models import Project, ToDo


class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

class Query(graphene.ObjectType):
    all_todo = graphene.List(TodoType)

    def resolve_all_todo(root, info):
        return ToDo.objects.all()


schema = graphene.Schema(query=Query)
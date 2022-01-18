from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectSerializer, TodoSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework import status


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                          mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = ProjectLimitOffsetPagination

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = Project.objects.all()
        if name:
            projects = Project.objects.filter(name__contains=name)
        return projects


class TodoModelViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                       mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                       mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoLimitOffsetPagination

    def get_queryset(self):
        project = self.request.query_params.get('project', '')
        todo = ToDo.objects.all()
        if project:
            todo = ToDo.objects.filter(project=project)
        return todo

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_active == True:
            instance.is_active = False
            instance.save()
        return Response(status=status.HTTP_200_OK)

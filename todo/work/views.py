from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectSerializer, TodoSerializer
from rest_framework.pagination import PageNumberPagination

class ProjectPagination(PageNumberPagination):
    page_size = 20

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    pagination_class = ProjectPagination
    serializer_class = ProjectSerializer


class TodoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
from django.shortcuts import render
from rest_framework import filters
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from task.models import Task
from task.serializers import TaskSerializer

class TaskAllView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('task_name', 'created_at', 'updated_at', 'created_by', 'responsible_user')


class TaskCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

class MyTasksView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

class UpdateTaskView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)
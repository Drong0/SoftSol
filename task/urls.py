from django.urls import path, include
from . import views

urlpatterns = [
    path('tasks', views.TaskAllView.as_view(), name='tasks'),
    path('tasks/mytasks', views.MyTasksView.as_view(), name='mytasks'),
    path('tasks/<int:pk>', views.UpdateTaskView.as_view(), name='task'),
]

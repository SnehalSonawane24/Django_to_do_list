from django.urls import path
from .views import TaskList, TaskDetail, CreateTask, UpdateTask, DeleteTask
from base import views

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task' ),
    path('task-create/', CreateTask.as_view(), name='task-create'),
    path('task-update/<int:pk>/', UpdateTask.as_view(), name='task-update' ),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),
    
]

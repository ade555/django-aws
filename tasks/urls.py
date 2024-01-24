from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskListCreate.as_view(), name="list-create-task"),
    path('modify/<int:task_id>/', views.TaskRetrieveUpdateDelete.as_view(), name="task-retrieve-update")
]

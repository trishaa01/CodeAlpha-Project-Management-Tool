from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('create/<int:project_pk>/', views.create_task, name='create'),
    path('<int:pk>/', views.task_detail, name='detail'),
    path('<int:pk>/update/', views.update_task, name='update'),
    path('<int:pk>/delete/', views.delete_task, name='delete'),
    path('<int:pk>/status/', views.update_task_status, name='update_status'),
]
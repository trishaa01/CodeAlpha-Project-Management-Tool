from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_project, name='create'),
    path('<int:pk>/', views.project_detail, name='detail'),
    path('<int:pk>/invite/', views.invite_member, name='invite'),
    path('<int:pk>/delete/', views.delete_project, name='delete'),
]
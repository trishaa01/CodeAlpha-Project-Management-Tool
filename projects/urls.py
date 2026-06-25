from django.urls import path
from django.http import HttpResponse

app_name = 'projects'

def coming_soon(request):
    return HttpResponse("<h2 style='font-family:sans-serif;padding:40px;color:#7c6ff7'>⚡ TaskFlow — Projects coming soon!</h2>")

urlpatterns = [
    path('', coming_soon, name='dashboard'),
]
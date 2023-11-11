from django.urls import path, include
from .views import OutputTasks

urlpatterns = [
    path('List', OutputTasks.as_view())
]
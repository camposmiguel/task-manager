"""todomanager URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('task_manager.urls')),

]

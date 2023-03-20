from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('completed/', views.completed, name='completed'),
    path('delete/<task_id>/', views.deleteTask, name='delete'),
    path('taskdonetrue/<task_id>', views.changeStatusTrue, name='statustrue'),
    path('taskdonefalse/<task_id>', views.changeStatusFalse, name='statusfalse'),
    path('edit/<id>', views.editTask, name='edit'),
]

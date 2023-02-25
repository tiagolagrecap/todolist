from django.urls import path
from .views import index, delete_task, update_task, done, undone

urlpatterns = [
    path('', index, name="index"),
    path('delete/<int:pk>/', delete_task, name="delete-task"),
    path('update/<int:pk>/', update_task, name="update-task"),
    path('done/<int:pk>/', done, name="done"),
    path('undone/<int:pk>/', undone, name="undone"),
]

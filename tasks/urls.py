from django.urls import path
from .views import list_tasks, delete_task, create_task, update_task
urlpatterns = [
    path('', list_tasks, name='list_tasks'),  # Asegúrate de que esta ruta tenga el nombre correcto
    path('new_task/', create_task, name='create_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
]

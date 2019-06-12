from django.urls import path
from . import views
urlpatterns = [
    path('', views.TodoList.as_view(), name='list_to_do'),
    path('todo/new/', views.TodoCreate.as_view(), name='new_to_do'),
    path('completed/<int:pk>/', views.completed, name='completed'),
]


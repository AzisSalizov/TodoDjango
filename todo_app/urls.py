from django.urls import path
from . import views

urlpatterns = [
    path('' , views.alltodos , name='home'),
    path('del-item/<int:pk>' , views.deleteTodo , name='del'),
    path('update-item<str:pk>' , views.updateTodo , name='updateItem'),
]

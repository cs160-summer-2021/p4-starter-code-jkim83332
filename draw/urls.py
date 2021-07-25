# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('interactive-user', views.interactive_user, name='interactive_user'),
    path('interactive-user2', views.interactive_user_2, name='interactive_user_2'),
    path('interactive-big', views.interactive_big, name='interactive_big'),
    path('interactive-big2', views.interactive_big2, name='interactive_big2'),
]

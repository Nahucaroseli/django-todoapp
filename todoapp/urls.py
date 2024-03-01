from django.urls import path
from todoapp import views




urlpatterns = [
    path('', views.home, name="Home"),
    path('add_task/',views.add_task, name='add_task/')
]
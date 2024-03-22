from django.urls import path
from todoapp import views




urlpatterns = [
    path('home', views.home, name="Home"),
    path('add_task/',views.add_task, name='add_task/'),
    path('delete_task/',views.delete_task, name='delete_task/'),
    path('modify_task/',views.modify_task, name='modify_task/'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin, name='signin'),
    path('logout',views.logout_view, name='logout')
    
]
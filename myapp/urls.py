from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index , name= "index"),
    path('hello/<str:username>', views.hello, name= "hello"),
    path('about/', views.about, name= "about"),
    path('tasks/<int:id>/', views.tasks , name="tasks"),
    path('tasks_form', views.tasks_form , name="tasks_form"),
    path('project', views.project , name= "projectos"),
    path('create_project', views.create_project , name= "crear_proyecto"),
    path('crear_usuario', views.crear_usuario, name= "nuevo_usuario"),
    path('registrarse', views.crear_usuario),
    path('logout', views.signout, name= "logout"),
    path('login', views.signin, name= "login"),
    path('update/<int:id>/', views.actualizar, name= "update"),
    path('update/<int:id>/delete', views.borrar_tarea, name= "delete"),
] 
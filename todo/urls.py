from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    
    path('admin/', admin.site.urls),

    #---------------------- Homepage ------------------------#
    #--------------------------------------------------------#

    path('', views.home, name=""),


    #-------------------- Register a user -----------------#
    #------------------------------------------------------#

    path('register', views.register, name="register"),


    #-------------------- Login a user --------------------#
    #------------------------------------------------------#
    
    path('my-login', views.my_login, name="my-login"),


    #-------------------- Dashboard -----------------------#
    #------------------------------------------------------#
    
    path('dashboard', views.dashboard, name="dashboard"),


    #-------------------- Create Task ---------------------#
    #------------------------------------------------------#
    
    path('create-task', views.createTask, name="create-task"),


    #----------------- View (Read) Task -------------------#
    #------------------------------------------------------#
    
    path('view-tasks', views.viewTask, name="view-tasks"),


    #-------------------- Update Task ---------------------#
    #------------------------------------------------------#
    
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),


    #-------------------- Delete Task ---------------------#
    #------------------------------------------------------#
    
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),



    #------------------- Logout a user --------------------#
    #------------------------------------------------------#
    
    path('user-logout', views.user_logout, name="user-logout"),

]

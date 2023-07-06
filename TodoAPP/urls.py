"""
URL configuration for TodoAPP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from TaskApp.views import register, task_list, task_create, task_update, task_delete,profile_view
from django.contrib.auth.views import LoginView, LogoutView
#from django.contrib.auth.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:task_id>/', task_update, name='task_update'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
]



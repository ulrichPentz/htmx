"""
URL configuration for htmx_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from sim import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.example, name='example'),
    path('createUser/', views.createUser, name='createUser'),
    path('updateUser/', views.updateUser, name='updateUser'),
    path('update_demographics/<id>', views.update_demographics, name='update_demographics'),
    path('deleteDemographics/<id>', views.deleteDemographics, name='deleteDemographics'),
]

"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from projects.views import (
    ProjectListCreateView,
    ProjectRetrieveUpdateDestroyView,
    ProjectUserAddView,
    UserProjectListView,
    InitiateScanView,
    LogoutView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('api/projects/<int:pk>/add-user/', ProjectUserAddView.as_view(), name='project-add-user'),
    path('api/user/<int:user_id>/projects/', UserProjectListView.as_view(), name='user-project-list'),
    path('api/scan/<int:project_id>/', InitiateScanView.as_view(), name='initiate-scan'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
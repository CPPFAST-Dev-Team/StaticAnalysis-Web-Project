from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView, UserProjectListView, ProjectUserAddView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('users/<int:user_id>/projects/', UserProjectListView.as_view(), name='user-projects'),
    path('projects/<int:pk>/users/', ProjectUserAddView.as_view(), name='project-add-user'),
]
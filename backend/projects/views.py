from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
import logging
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            logger.info(f"User {request.user.username} retrieved {queryset.count()} projects")
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error listing projects for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while retrieving projects"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            logger.info(f"User {request.user.username} created a new project: {response.data.get('name', 'Unknown')}")
            return response
        except Exception as e:
            logger.error(f"Error creating project for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while creating the project"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            logger.info(f"User {request.user.username} retrieved project: {instance.name}")
            return Response(serializer.data)
        except Project.DoesNotExist:
            logger.warning(f"User {request.user.username} attempted to retrieve non-existent project")
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving project for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while retrieving the project"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            logger.info(f"User {request.user.username} updated project: {response.data.get('name', 'Unknown')}")
            return response
        except Exception as e:
            logger.error(f"Error updating project for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while updating the project"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            project_name = instance.name
            self.perform_destroy(instance)
            logger.info(f"User {request.user.username} deleted project: {project_name}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Project.DoesNotExist:
            logger.warning(f"User {request.user.username} attempted to delete non-existent project")
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting project for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while deleting the project"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        

class UserProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Project.objects.filter(users__id=user_id)

class ProjectUserAddView(generics.UpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def update(self, request, *args, **kwargs):
        project = self.get_object()
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            project.users.add(user)
            return Response({"message": "User added to project successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        

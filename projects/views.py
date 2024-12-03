from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

class ProjectListCreateView(generics.ListCreateAPIView):
    """
    List all projects for the authenticated user or create a new project.

    This view provides GET and POST methods for projects.

    :param request: The HTTP request object.
    :type request: rest_framework.request.Request
    :return: A list of projects or the created project details.
    :rtype: rest_framework.response.Response
    :raises: Exception if there's an error during project listing or creation.
    """
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
            repo = request.data.get('repo')
            token = request.data.get('token')
            
            # Add logic here to validate repo and token
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            logger.info(f"User {request.user.username} created a new project: {serializer.data.get('name', 'Unknown')}")
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            logger.error(f"Error creating project for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while creating the project"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a project instance.

    This view provides GET, PUT, PATCH, and DELETE methods for a specific project.

    :param request: The HTTP request object.
    :type request: rest_framework.request.Request
    :param pk: The primary key of the project.
    :type pk: int
    :return: The project details, updated project details, or a success message.
    :rtype: rest_framework.response.Response
    :raises: Project.DoesNotExist if the project is not found.
    :raises: Exception if there's an error during project operations.
    """
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
    """
    List all projects for a specific user.

    This view provides a GET method to retrieve all projects associated with a given user.

    :param request: The HTTP request object.
    :type request: rest_framework.request.Request
    :param user_id: The ID of the user whose projects are to be listed.
    :type user_id: int
    :return: A list of projects associated with the specified user.
    :rtype: rest_framework.response.Response
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Project.objects.filter(users__id=user_id)

class ProjectUserAddView(generics.UpdateAPIView):
    """
    Add a user to a specific project.

    This view provides a PUT method to add a user to a project.

    :param request: The HTTP request object.
    :type request: rest_framework.request.Request
    :param pk: The primary key of the project.
    :type pk: int
    :return: A success message if the user is added, or an error message if the user is not found.
    :rtype: rest_framework.response.Response
    :raises: User.DoesNotExist if the specified user is not found.
    """
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

class InitiateScanView(generics.CreateAPIView):
    """
    Initiate a scan for a specific project.

    This view provides a POST method to start a scan for a project.

    :param request: The HTTP request object.
    :type request: rest_framework.request.Request
    :param project_id: The ID of the project to be scanned.
    :type project_id: int
    :return: A success message if the scan is initiated, or an error message if the project is not found.
    :rtype: rest_framework.response.Response
    :raises: Project.DoesNotExist if the specified project is not found.
    """
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        project_id = kwargs.get('project_id')
        branch = request.data.get('branch')
        commit = request.data.get('commit')

        try:
            project = Project.objects.get(id=project_id, owner=request.user)
            # Add logic here to initiate the scan
            # Update issue counts based on scan results
            return Response({"message": "Scan initiated successfully"}, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error initiating scan for project {project_id}: {str(e)}")
            return Response({"error": "An error occurred while initiating the scan"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class LogoutView(generics.GenericAPIView):
    """
    Logout the user.

    This view provides a POST method to log out the user.

    :param request: The HTTP request object.
    :type request: rest_framework.request.Request
    :return: A success message if the user is logged out.
    :rtype: rest_framework.response.Response
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Add logic here to log out the user
        return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)

#class LogoutView(APIView):
#    """
#    API view for user logout.
#
#    This view handles POST requests for user logout by removing the user's token.
#    
#    :param request: The HTTP request object.
#    :type request: rest_framework.request.Request
#    :return: Response indicating successful logout.
#    :rtype: rest_framework.response.Response
#    """
#    permission_classes = [IsAuthenticated] # Add this line to require authentication
#
#    def post(self, request):
#        # Optionally handle token blacklisting here if needed
#        return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
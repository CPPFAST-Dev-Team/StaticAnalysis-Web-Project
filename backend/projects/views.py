"""
Projects views module.

This module contains API views for managing projects,
initiating code scans, listing vulnerabilities, and handling user logout.
"""

import os
import tempfile
import logging

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .models import Project, Vulnerability
from . import serializers

logger = logging.getLogger(__name__)


class ProjectListCreateView(generics.ListCreateAPIView):
    """
    List all projects for the authenticated user or create a new project.

    This view provides GET and POST methods for projects.

    :cvar queryset: All projects in the system.
    :cvar serializer_class: Serializer class for project objects.
    :cvar permission_classes: List of permission classes required.
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a queryset of projects owned by the authenticated user.

        :return: QuerySet of Project instances.
        :rtype: django.db.models.query.QuerySet
        """
        return Project.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Save the new project setting the authenticated user as owner.

        :param serializer: The project serializer instance.
        :type serializer: ProjectSerializer
        """
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        List projects owned by the authenticated user.

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response containing the list of projects.
        :rtype: rest_framework.response.Response
        """
        try:
            queryset = self.get_queryset()
            logger.info(f"User {request.user.username} retrieved {queryset.count()} projects")
            return super().list(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error listing projects for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while retrieving projects"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        """
        Create a new project for the authenticated user.

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response containing the created project data.
        :rtype: rest_framework.response.Response
        """
        try:
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
    Retrieve, update or delete a specific project instance.

    This view provides GET, PUT, PATCH, and DELETE methods for a project.

    :cvar queryset: All projects in the system.
    :cvar serializer_class: Serializer class for project objects.
    :cvar permission_classes: List of permission classes required.
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a queryset of projects owned by the authenticated user.

        :return: QuerySet of Project instances.
        :rtype: django.db.models.query.QuerySet
        """
        return Project.objects.filter(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve details of a specific project.

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response containing project details.
        :rtype: rest_framework.response.Response
        """
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
        """
        Update a specific project.

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response containing updated project data.
        :rtype: rest_framework.response.Response
        """
        try:
            response = super().update(request, *args, **kwargs)
            logger.info(f"User {request.user.username} updated project: {response.data.get('name', 'Unknown')}")
            return response
        except Exception as e:
            logger.error(f"Error updating project for user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred while updating the project"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        """
        Delete a specific project.

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response with HTTP 204 status code.
        :rtype: rest_framework.response.Response
        """
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
    List projects for a specific user.

    This view returns all projects associated with a given user ID.

    :cvar serializer_class: Serializer class for project objects.
    """
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        """
        Return a queryset of projects for the specified user.

        :return: QuerySet of Project instances.
        :rtype: django.db.models.query.QuerySet
        """
        user_id = self.kwargs['user_id']
        return Project.objects.filter(users__id=user_id)


class ProjectUserAddView(generics.UpdateAPIView):
    """
    Add a user to a specific project.

    This view supports adding an existing user (by user_id) to a project.

    :cvar queryset: All projects in the system.
    :cvar serializer_class: Serializer class for project objects.
    """
    queryset = Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    def update(self, request, *args, **kwargs):
        """
        Add a user to the project specified by the primary key.

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response with a success message.
        :rtype: rest_framework.response.Response
        :raises User.DoesNotExist: If the specified user is not found.
        """
        project = self.get_object()
        user_id = request.data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            project.users.add(user)
            return Response({"message": "User added to project successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


def send_to_scanner(zip_file_path):
    """
    Simulate a tRPC call to a scanner container.

    In production, this function would implement real tRPC client logic.
    It returns a dummy SARIF (Static Analysis Results Interchange Format) JSON structure.

    :param zip_file_path: The file path to the uploaded ZIP file.
    :type zip_file_path: str
    :return: A dummy SARIF JSON result.
    :rtype: dict
    """
    return {
        "version": "2.1.0",
        "runs": [{
            "tool": {"driver": {"name": "DummyScanner"}},
            "results": []
        }]
    }


class InitiateScanView(generics.CreateAPIView):
    """
    Initiate a static code analysis scan for a project.

    This view accepts a ZIP file upload containing the code to be scanned.
    It simulates sending the file via a tRPC interface to a scanner container,
    and stores the returned SARIF JSON result in an AnalysisResult.

    :cvar parser_classes: List of parsers to handle multipart/form data.
    """
    parser_classes = [MultiPartParser, FormParser]

    def create(self, request, *args, **kwargs):
        """
        Initiate a scan for a specified project.

        The request must include 'project_id' and a ZIP file under the key 'file'.

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response containing the analysis ID and results.
        :rtype: rest_framework.response.Response
        """
        project_id = request.data.get('project_id')
        zip_file = request.FILES.get('file')

        if not project_id or not zip_file:
            return Response({"error": "project_id and file are required"}, status=status.HTTP_400_BAD_REQUEST)

        if not zip_file.name.lower().endswith('.zip'):
            return Response({"error": "File must be a zip file"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp:
            for chunk in zip_file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name

        try:
            sarif_result = send_to_scanner(tmp_path)
        except Exception as e:
            os.remove(tmp_path)
            return Response({"error": f"Scanning error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        os.remove(tmp_path)
        analysis = project.analysis_results.create(status="COMPLETED", result=sarif_result)
        return Response({"analysis_id": analysis.id, "result": sarif_result}, status=status.HTTP_201_CREATED)


class ProjectVulnerabilitiesListView(generics.ListAPIView):
    """
    List all vulnerabilities for a specific project with severity color coding.

    The response will include a computed "color" field per vulnerability:
       - LOW: green,
       - MEDIUM: yellow,
       - SEVERE: red.

    This is used to easily present severity levels in the frontend.
    """
    serializer_class = serializers.VulnerabilitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return vulnerabilities that belong to the requested project.
        
        The project ID is taken from the URL keyword arguments.
        
        :return: QuerySet of Vulnerability instances for the project.
        :rtype: django.db.models.query.QuerySet
        """
        project_id = self.kwargs.get('project_id')
        return Vulnerability.objects.filter(project_id=project_id)


class LogoutView(generics.GenericAPIView):
    """
    Log out the user by blacklisting the provided refresh token.

    This view requires the client to send a valid refresh token in the request data.
    The refresh token is blacklisted to ensure it cannot be used again.

    :cvar permission_classes: List containing IsAuthenticated.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handle POST request to log out the user.

        The request must include the refresh token under the key "refresh".

        :param request: The HTTP request instance.
        :type request: rest_framework.request.Request
        :return: Response indicating successful logout.
        :rtype: rest_framework.response.Response
        :raises KeyError: If the refresh token is not provided.
        :raises Exception: For any other errors during logout.
        """
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            logger.info(f"User {request.user.username} logged out successfully.")
            return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
        except KeyError:
            logger.error(f"Logout error: Refresh token not provided by user {request.user.username}.")
            return Response({"error": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error logging out user {request.user.username}: {str(e)}")
            return Response({"error": "An error occurred during logout"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
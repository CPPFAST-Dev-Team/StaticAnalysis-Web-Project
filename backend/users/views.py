import os
import requests

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer, GithubAuthSerializer, GithubReposSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    This view handles POST requests to create a new user account.
    """
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user registration.

        :param request: The HTTP request object
        :type request: rest_framework.request.Request
        :return: Response with user data and JWT tokens on success, or error messages on failure
        :rtype: rest_framework.response.Response
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    """
    API view for user login.

    This view handles POST requests to authenticate a user and return JWT tokens.
    """
    def post(self, request):
        """
        Handle POST request for user login.

        :param request: The HTTP request object
        :type request: rest_framework.request.Request
        :return: Response with JWT tokens on success, or error messages on failure
        :rtype: rest_framework.response.Response
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user': UserSerializer(user).data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(APIView):
    """
    API view for user logout.

    This view handles POST requests for user logout by deleting the user's auth token.
    """
    def post(self, request):
        """
        Handle POST request for user logout.

        :param request: The HTTP request object
        :type request: rest_framework.request.Request
        :return: Response indicating successful logout
        :rtype: rest_framework.response.Response
        """
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
    
class GithubAuthAPIView(APIView):
    """
    Exchange GitHub OAuth 'code' for an access token, fetch the user profile,
    create/login user, and return JWT.
    """

    def post(self, request, *args, **kwargs):
        code = request.data.get("code")
        if not code:
            return Response({"error": "Code not provided"}, status=status.HTTP_400_BAD_REQUEST)

        # Step 1: Exchange the code for an access token
        token_url = "https://github.com/login/oauth/access_token"
        payload = {
            "client_id": os.getenv("GITHUB_CLIENT_ID"),
            "client_secret": os.getenv("GITHUB_SECRET_KEY"),
            "code": code,
            "redirect_uri": os.getenv("GITHUB_REDIRECT_URI"),
        }
        headers = {"Accept": "application/json"}

        token_res = requests.post(token_url, data=payload, headers=headers)
        token_data = token_res.json()

        access_token = token_data.get("access_token")
        if not access_token:
            return Response({"error": "Failed to retrieve access token", "details": token_data},
                            status=status.HTTP_400_BAD_REQUEST)

        # Step 2: Use the access token to fetch GitHub profile
        # TODO: Retrieve additional profile info if necessary
        user_res = requests.get(
            "https://api.github.com/user",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        profile = user_res.json()

        if "id" not in profile:
            return Response({"error": "Failed to fetch GitHub profile", "details": profile},
                            status=status.HTTP_400_BAD_REQUEST)

        username = profile.get("login")

        # Step 3: Get or create a local user
        # TODO: Handle potential username conflicts and create UserProfile if necessary
        user, _ = User.objects.get_or_create(username=username)

        # Step 4: Generate JWT
        refresh = RefreshToken.for_user(user)

        # Step 5: Serialize and respond
        data = {
            "access": str(refresh.access_token),
            "user_id": user.id,
            "username": user.username,
        }
        serializer = GithubAuthSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GithubReposListView(APIView):
    """
    API view to fetch and return a list of Github repositiries for a given user
    """
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        github_username = user.username

        # Fetch repositories from Github API
        repos_url = f"https://api.github.com/users/{github_username}/repos"
        response = requests.get(repos_url)
        if response.status_code != 200:
            return Response({"error": "Failed to fetch repositories from GitHub"}, status=response.status_code)
        repos = response.json()

        # Serialize and return the repo data
        data = []
        for repo in repos:
            data.append({
                "id": repo["id"],
                "name": repo["name"],
                "language": repo["language"] if repo["language"] else None,
                "repository_url": repo["html_url"],
            })
        serializer = GithubReposSerializer(data=data, many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)
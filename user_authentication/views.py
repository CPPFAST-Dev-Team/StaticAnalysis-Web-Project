from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    API view for user registration.

    This view handles POST requests to create a new user account.

    :param request: The HTTP request object
    :type request: rest_framework.request.Request
    :return: Response with user data and JWT tokens on success, or error messages on failure
    :rtype: rest_framework.response.Response
    """
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle POST request for user registration.

        :param request: The HTTP request object
        :type request: rest_framework.request.Request
        :param args: Additional positional arguments
        :param kwargs: Additional keyword arguments
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

    :param request: The HTTP request object
    :type request: rest_framework.request.Request
    :return: Response with JWT tokens on success, or error messages on failure
    :rtype: rest_framework.response.Response
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

class LogoutView(generics.GenericAPIView):
    """
    API view for user logout.

    This view handles POST requests for user logout by deleting the user's auth token.

    :param request: The HTTP request object
    :type request: rest_framework.request.Request
    :return: Response indicating successful logout
    :rtype: rest_framework.response.Response
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
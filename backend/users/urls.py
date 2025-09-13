from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, GithubAuthAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('github/', GithubAuthAPIView.as_view(), name='github'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
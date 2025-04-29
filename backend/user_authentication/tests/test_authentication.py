from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import status # Add this import if you want to check the status code of the response

class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
    
    def test_token_authentication(self):
        refresh = RefreshToken.for_user(self.user)
        
        # Access a protected endpoint with the token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        
        # Replace '/protected-endpoint/' with an actual endpoint that requires authentication
        response = self.client.get('/protected-endpoint/')
        
        # Adjust expected status code based on your endpoint's behavior
        self.assertEqual(response.status_code, status.HTTP_200_OK)
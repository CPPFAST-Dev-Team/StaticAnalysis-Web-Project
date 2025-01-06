from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from projects.models import Project
from rest_framework_simplejwt.tokens import RefreshToken

class SimpleTestCase(TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)
        self.project = Project.objects.create(
            name='Test Project',
            description='A test project description',
            repository_url='https://example.com/repo.git',
            owner=self.user
        )

    def test_create_project(self):
        """
        Test creating a new project.
        """
        url = reverse('project-list-create')
        data = {
            'name': 'New Project',
            'description': 'New project description',
            'repository_url': 'https://example.com/repo.git',
            'owner': self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_projects(self):
        """
        Test listing projects.
        """
        url = reverse('project-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_authentication(self):
        """
        Test token authentication.
        """
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get(reverse('project-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
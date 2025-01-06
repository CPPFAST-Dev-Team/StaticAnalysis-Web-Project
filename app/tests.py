import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.server.settings'

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from projects.models import Project
from rest_framework_simplejwt.tokens import RefreshToken
from static_analysis.models import AnalysisResult

class ProjectTests(TestCase):
    """
    Test cases for the Project views.
    """
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

    def test_list_projects(self):
        """
        Test listing projects.
        """
        url = reverse('project-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project(self):
        """
        Test creating a new project.
        """
        url = reverse('project-list-create')
        data = {'name': 'New Project', 'description': 'New project description', 'repository_url': 'https://example.com/repo.git'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class StaticAnalysisTests(TestCase):
    """
    Test cases for the Static Analysis views.
    """
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

    def test_initiate_analysis(self):
        """
        Test initiating a static analysis.
        """
        url = reverse('initiate-analysis', kwargs={'pk': self.project.id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_analysis_results(self):
        """
        Test retrieving static analysis results.
        """
        AnalysisResult.objects.create(
            project=self.project,
            status='COMPLETED',
            result={'issues': []}
        )
        url = reverse('analysis-results', kwargs={'pk': self.project.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserAuthenticationTests(TestCase):
    """
    Test cases for the User Authentication views.
    """
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_user_registration(self):
        """
        Test user registration.
        """
        url = reverse('user-register')
        data = {'username': 'newuser', 'password': 'newpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        """
        Test user login.
        """
        url = reverse('user-login')
        data = {'username': 'testuser', 'password': 'testpass123'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_authentication(self):
        """
        Test token authentication.
        """
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.get(reverse('project-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)